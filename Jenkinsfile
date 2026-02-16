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
        stage('GitOps Sync Notification') {
            steps {
                // NOTA: Ejecutamos fuera de 'container(docker)' para usar el git del agente base
                sh "git clone https://github.com/anfedimo/kubernetes-u-sabana.git"
                dir('kubernetes-u-sabana') {
                    sh "sed -i 's/tag: .*/tag: \"${BUILD_NUMBER}\"/' charts/sabana-api/values.yaml"
                    
                    withCredentials([usernamePassword(credentialsId: 'github-creds-sabana', 
                                                     usernameVariable: 'GIT_USER', 
                                                     passwordVariable: 'GIT_TOKEN')]) {
                        sh "git config user.email 'jenkins@sabana.edu.co'"
                        sh "git config user.name 'Jenkins Bot'"
                        sh "git add charts/sabana-api/values.yaml"
                        sh "git commit -m 'GitOps: Update image to build ${BUILD_NUMBER}'"
                        sh "git push https://${GIT_TOKEN}@github.com/anfedimo/kubernetes-u-sabana.git main"
                    }
                }
            }
        }
    }
}