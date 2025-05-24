#!/bin/bash

SONARQUBE_URL=http://localhost:9000
PROJECT_BASE_DIR=sonarqube-fastapi
SONARQUBE_PROJECT_KEY=fastapi
SONARQUBE_TOKEN=sqp_f03c2bf4e9bd3319f6efb5139518338a3b318811

docker run \
		--network=host \
    --platform linux/amd64 \
		-v $PWD:/$PROJECT_BASE_DIR \
		-e SONAR_HOST_URL="$SONARQUBE_URL" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$SONARQUBE_PROJECT_KEY \
		-Dsonar.login=$SONARQUBE_TOKEN \
		-Dsonar.coverage.dtdVerification=false \
		-Dsonar.python.version=3.12 \
		-Dsonar.python.coverage.reportPaths=/coverage.xml \
		-Dsonar.python.xunit.reportPath=/result.xml \
		-Dsonar.inclusions=/task_manager/**/*.py \
		-Dsonar.projectBaseDir=/$PROJECT_BASE_DIR \
		-Dsonar.coverage.exclusions=/**/__init__.py,/**/test_*.py" \
		sonarsource/sonar-scanner-cli	 

