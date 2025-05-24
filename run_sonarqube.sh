#!/bin/bash

PROJECT_BASE_DIR=task_manager
SONARQUBE_URL=http://localhost:9000
SONARQUBE_PROJECT_KEY=fastapi
SONARQUBE_TOKEN=sqp_f03c2bf4e9bd3319f6efb5139518338a3b318811


docker run \
		--network=host \
		-v $PWD:/$PROJECT_BASE_DIR \
		-e SONAR_HOST_URL="$SONARQUBE_URL" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$SONARQUBE_PROJECT_KEY -Dsonar.login=$SONARQUBE_TOKEN -Dsonar.projectBaseDir=/$PROJECT_BASE_DIR" \
		sonarsource/sonar-scanner-cli	

