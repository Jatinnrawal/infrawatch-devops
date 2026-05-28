pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'YOUR_GITHUB_REPO_URL'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t infrawatch .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh './scripts/deploy.sh'
            }
        }

        stage('Health Check') {
            steps {
                sh './scripts/health_check.sh'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}