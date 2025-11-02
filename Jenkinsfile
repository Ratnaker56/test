pipeline {
    agent any
    stages {
        // ... (Stages 1, 2, 3 are the same) ...

        stage('1: Clone Code') {
            steps {
                echo 'Code was automatically cloned by the job.'
            }
        }
        stage('2: Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t 377733340897.dkr.ecr.eu-north-1.amazonaws.com/my-devops-app:latest .'
                }
            }
        }
        stage('3: Push to AWS ECR') {
            steps {
                script {
                    withAWS(credentials: 'aws-creds', region: 'eu-north-1') {
                        sh 'aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 377733340897.dkr.ecr.eu-north-1.amazonaws.com'
                        sh 'docker push 377733340897.dkr.ecr.eu-north-1.amazonaws.com/my-devops-app:latest'
                    }
                }
            }
        }

        // --- STAGE 4: DEPLOY (The new code) ---
        stage('4: Deploy to ECS') {
             steps {
                echo 'Image pushed! Starting deployment...'
                script {
                    // Use the same AWS credentials and region
                    withAWS(credentials: 'aws-creds', region: 'eu-north-1') {
                        
                        // This is the magic command:
                        // It tells your 'my-app-service' in 'my-cluster' to restart,
                        // forcing it to pull the 'latest' image you just pushed.
                        sh 'aws ecs update-service --cluster my-cluster --service my-app-service --force-new-deployment'
                    }
                }
             }
        }
    }
}
