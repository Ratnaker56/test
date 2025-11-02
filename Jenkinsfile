pipeline {
    // 1. Tell Jenkins to use any available agent
    agent any

    // 2. Define all the stages of your pipeline
    stages {

        // --- STAGE 1: CLONE ---
        // Get the code from your GitHub repository
        stage('1: Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Ratnaker56/test/'
            }
        }

        // --- STAGE 2: BUILD ---
        // Build your Docker image using the Dockerfile in your repo
        stage('2: Build Docker Image') {
            steps {
                script {
                    // This command builds the image and tags it with your ECR repository URI
                    // '377733340897.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest'
                    sh 'docker build -t 377733340897.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest .'
                }
            }
        }

        // --- STAGE 3: PUSH TO ECR ---
        // Log in to AWS and push the image to your private registry (ECR)
        stage('3: Push to AWS ECR') {
            steps {
                script {
                    // This 'withAWS' block uses the 'aws-creds' you created in Jenkins
                    withAWS(credentials: 'aws-creds', region: 'us-east-1') {
                        
                        // Step 3a: Get a login password from AWS ECR
                        sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 377733340897.dkr.ecr.us-east-1.amazonaws.com'
                        
                        // Step 3b: Push the image
                        sh 'docker push 377733340897.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest'
                    }
                }
            }
        }

        // --- STAGE 4: DEPLOY (Placeholder) ---
        // This is where you would add steps to deploy to ECS
        stage('4: Deploy') {
             steps {
                echo 'Image pushed to ECR! Ready to deploy.'
             }
        }
    }
}
