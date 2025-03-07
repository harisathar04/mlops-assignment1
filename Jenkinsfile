pipeline {
    agent any
    stages {

        
        stage('Clone Repository') {
            steps {
                git 'https://github.com/harisathar04/mlops-assignment1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-app .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker tag mlops-app riyaantariq/mlops-app:latest'
                    sh 'docker push riyaantariq/mlops-app:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5001:5001 riyaantariq/mlops-app:latest'
            }
        }

        stage('Notify Admin') {
            steps {
                mail bcc: '56riyaan@gmail.com', body: 'Deployment Successful', from: 'jenkins@example.com', subject: 'Deployment Complete', to: 'harisathar04@gmail.com'
            }
        }
    }
}