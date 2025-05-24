pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    cd sonarqube-fastapi
                    echo "Running tests..."
                    ./run_tests.sh
                '''
            }
        }

        stage('SonarQube Analysis') { 
            steps {
                sh '''
                    cd sonarqube-fastapi
                    echo "Running sonarqube..."
                    ./run_sonarqube.sh
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
            }
        }
    }
}

