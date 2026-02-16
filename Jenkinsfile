pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'anfedimo'
        APP_NAME = 'devops-dev-sabana-backend'
        IMAGE_TAG = "${DOCKERHUB_USER}/${APP_NAME}:${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Clona el backend para compilar
            }
        }
        stage('Docker Build') {
            steps {
                // Construye la imagen usando el Dockerfile del backend
                sh "docker build -t ${IMAGE_TAG} ."
            }
        }
        stage('Push to DockerHub') {
            steps {
                // Publica la imagen inmutable
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                                                 usernameVariable: 'USER', 
                                                 passwordVariable: 'PASS')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${IMAGE_TAG}"
                    sh "docker tag ${IMAGE_TAG} ${DOCKERHUB_USER}/${APP_NAME}:latest"
                    sh "docker push ${DOCKERHUB_USER}/${APP_NAME}:latest"
                }
            }
        }
        stage('GitOps Sync Notification') {
            steps {
                echo "Imagen publicada. ArgoCD detectará el cambio y actualizará el clúster."
            }
        }
    }
}