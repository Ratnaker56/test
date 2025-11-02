pipeline {
    agent any
    stages {
        // Stage 1: Checkout code (This is handled by "Pipeline from SCM")
        // We can remove the extra 'git' step to make it cleaner.
        stage('1: Clone Code') {
            steps {
                echo 'Code was automatically cloned by the job.'
            }
        }

        // Stage 2: Build the Docker image
        stage('2: Build Docker Image') {
            steps {
                script {
                    // ✅ FIXED: Using your region 'eu-north-1'
                    sh 'docker build -t 377733340897.dkr.ecr.eu-north-1.amazonaws.com/my-devops-app:latest .'
                }
            }
        }

        // Stage 3: Push the image to ECR
        stage('3: Push to AWS ECR') {
            steps {
                script {
                    // ✅ FIXED: Using your region 'eu-north-1'
                    withAWS(credentials: 'aws-creds', region: 'eu-north-1') {
                        
                        // ✅ FIXED: Using your region 'eu-north-1'
                        sh 'aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 377733340897.dkr.ecr.eu-north-1.amazonaws.com'
                        
                        // ✅ FIXED: Using your region 'eu-north-1'
                        sh 'docker push 377733340897.dkr.ecr.eu-north-1.amazonaws.com/my-devops-app:latest'
                    }
                }
            }
        }

        // Stage 4: Deploy
        stage('4: Deploy') {
             steps {
                echo 'Image pushed to ECR! Ready to deploy.'
             }
        }
    }
}
