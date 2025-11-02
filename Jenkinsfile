// This is your Jenkinsfile
pipeline {
    agent any // Run this pipeline on any available Jenkins agent

    stages {
        stage('1: Clone Code') {
            // This step is now handled automatically by the "Pipeline from SCM" setting.
            // But if you needed to pull from a *different* repo, you could add a git step here.
            steps {
                echo 'Code automatically cloned.'
            }
        }
        
        stage('2: Build Docker Image') {
            steps {
                script {
                    // Make sure to replace these values with your AWS Account ID and ECR repo name
                    sh 'docker build -t 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest .'
                }
            }
        }

        stage('3: Push to AWS ECR') {
            steps {
                script {
                    // This 'your-aws-credentials-id' MUST match the ID you create in Manage Jenkins -> Credentials
                    withAWS(credentials: 'your-aws-credentials-id', region: 'us-east-1') {
                        // This command gets a temporary login password from AWS ECR
                        sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com'
                        
                        // This command pushes your new image to the repository
                        sh 'docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-devops-app:latest'
                    }
                }
            }
        }

        stage('4: Deploy') {
             steps {
                echo 'Image pushed to ECR. Next step would be to update an ECS service.'
                // For now, we'll stop here. Pushing to ECR is a huge success.
             }
        }
    }
}
