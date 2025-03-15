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

        post {
            success {
                script {
                    echo "Sending email to harisathar04@gmail.com..."
                    emailext(
                        subject: 'Build Success',
                        body: 'The Jenkins build was successful!',
                        to: 'harisathar04@gmail.com',
                        debug: true
                    )
                    echo "Email sent successfully."
                }
            }
        }
    }
}
