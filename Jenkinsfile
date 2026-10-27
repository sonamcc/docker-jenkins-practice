
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the Jenkins workspace'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t docker-practice:jenkins-%BUILD_NUMBER% .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat 'docker image inspect docker-practice:jenkins-%BUILD_NUMBER%'
            }
        }
    }

    post {
        success {
            echo 'Docker image built successfully!'
        }
        failure {
            echo 'Build failed. Check Console Output.'
        }
    }
}
