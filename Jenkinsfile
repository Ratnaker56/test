pipeline {
    agent any
    stages {
        stage('1: Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Ratnaker56/test/'
            }
        }
        stage('2: Build Docker Image') {
            steps {
                script {
                    // Use your AWS Account ID and ECR repo name
                    sh 'docker build -t 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest .'
                }
            }
        }
        stage('3: Push to AWS ECR') {
            steps {
                script {
                    // Use your Jenkins credential ID for AWS
                    withAWS(credentials: 'Rkwap@1234', region: 'us-east-1') {
                        // Logs in to ECR and pushes the image
                        sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com'
                        sh 'docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest'
                    }
                }
            }
        }
        stage('4: Deploy to ECS') {
             // For a quick practice, just pushing to ECR is a huge win.
             // Deploying to ECS Fargate is the next step if you have time.
             // It involves updating a Task Definition and Service.
             steps {
                echo 'Image pushed to ECR. Ready to deploy!'
             }
        }
    }
}
