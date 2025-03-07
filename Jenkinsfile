pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/sentiment-analysis-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sentiment-analysis-app .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker tag sentiment-analysis-app your-dockerhub-username/sentiment-analysis-app'
                    sh 'docker push your-dockerhub-username/sentiment-analysis-app'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 your-dockerhub-username/sentiment-analysis-app'
            }
        }

        stage('Notify Admin') {
            steps {
                mail bcc: '', body: 'Deployment Successful', from: 'jenkins@example.com', subject: 'Deployment Complete', to: 'harisathar04@gmail.com'
            }
        }
    }
}