pipeline {
    agent any
    stages {
        // Installs required Python dependencies for the pipeline environment.
        stage('Setup') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        // Runs unit tests. The pipeline will fail immediately if any test fails.
        stage('Validate Application') {
            steps {
                bat 'python -m pytest tests/'
            }
        }
        // Prepares the release artifact by zipping the source code into a dist folder
        stage('Package Release') {
            steps {
                bat 'if not exist dist mkdir dist'
                bat 'powershell Compress-Archive -Path src -DestinationPath dist/release-v1.zip -Force'
            }
        }
        // Archives the generated artifact so it can be downloaded from the Jenkins UI
        stage('Archive Release') {
            steps {
                archiveArtifacts artifacts: 'dist/*.zip', fingerprint: true
            }
        }
        // Validates that the Docker image builds successfully
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t vehicle-valuation:latest .'
            }
        }
    }
}