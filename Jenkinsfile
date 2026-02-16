pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:24.0.7-cli
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
'''
        }
    }
    environment {
        DOCKERHUB_USER = 'anfedimo'
        APP_NAME = 'devops-dev-sabana-backend'
        IMAGE_TAG = "${DOCKERHUB_USER}/${APP_NAME}:${BUILD_NUMBER}"
    }
    stages {
        stage('Docker Build') {
            steps {
                // Ejecutamos el comando dentro del contenedor 'docker' definido arriba
                container('docker') {
                    sh "docker build -t ${IMAGE_TAG} ."
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                container('docker') {
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
        }
    }
}