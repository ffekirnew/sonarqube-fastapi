#!/bin/bash

SONARQUBE_URL=http://localhost:9000
PROJECT_BASE_DIR=sonarqube-fastapi
SONARQUBE_PROJECT_KEY=fastapi
SONARQUBE_TOKEN=sqp_f03c2bf4e9bd3319f6efb5139518338a3b318811

pwd
ls .
mkdir -p /opt/sonar-scanner/conf
ls /opt/sonar-scanner/conf
cp sonar-project.properties /opt/sonar-scanner/conf/sonar-scanner.properties
cat /opt/sonar-scanner/conf/sonar-scanner.properties

docker run \
		--network=host \
    --platform linux/amd64 \
		-v $PWD:/$PROJECT_BASE_DIR \
		-e SONAR_HOST_URL="$SONARQUBE_URL" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=$SONARQUBE_PROJECT_KEY -Dsonar.login=$SONARQUBE_TOKEN -Dsonar.projectBaseDir=/$PROJECT_BASE_DIR" \
		sonarsource/sonar-scanner-cli	

