include .env

.PHONY: init_swarm leave_swarm sonarqube.start sonarqube.stop sonarqube.scan sonarqube.scan.docker sonarqube.scan.docker.log jenkins.start fastapi.run test.run test.coverage test.coverage.report activate_venv
PROJECT_BASE_DIR=task_manager

fastapi.run:
	@echo "Running FastAPI..."
	@fastapi dev task_manager/src/main.py

test.docker.build:
	@echo "Building Docker image for tests..."
	@docker build -t fastapi-test -f Dockerfile.test .

test.docker.run: test.docker.build
	@echo "Running tests in Docker..."
	@docker run --rm fastapi-test

test.run:
	@echo "Running tests..."
	@python -m pytest $(PROJECT_BASE_DIR)

test.coverage:
	@echo "Running tests with coverage..."
	@python -m pytest --cov=src --cov-report=term-missing $(PROJECT_BASE_DIR)

test.coverage.report:
	@echo "Generating coverage report..."
	@python -m pytest --cov-report xml:coverage.xml --cov=src --junitxml=result.xml $(PROJECT_BASE_DIR)

sonarqube.scan.docker: test.coverage.report
	@echo "Running SonarScanner in Docker..."
	@docker run \
		--network=host \
		-v $(PWD):/$(PROJECT_BASE_DIR) \
		-e SONAR_HOST_URL="$(SONARQUBE_URL)" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$(SONARQUBE_PROJECT_KEY) -Dsonar.login=$(SONARQUBE_TOKEN) -Dsonar.projectBaseDir=/$(PROJECT_BASE_DIR)" \
		sonarsource/sonar-scanner-cli

