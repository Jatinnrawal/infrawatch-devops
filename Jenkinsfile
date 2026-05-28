pipeline {
agent any

stages {

    stage('Clone Repository') {
        steps {
            git branch: 'main',
            url: 'https://github.com/Jatinnrawal/infrawatch-devops.git'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t infrawatch .'
        }
    }

    stage('Deploy Application') {
        steps {
            sh 'chmod +x scripts/deploy.sh'
            sh './scripts/deploy.sh'
        }
    }

    stage('Health Check') {
        steps {
            sh 'chmod +x scripts/health_check.sh'
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
