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
    stages {
        // ... (Tus etapas anteriores de Build y Push deben ir aquí) ...

        stage('GitOps Sync Notification') {
            steps {
                container('docker') {
                    // Clonar repo de infraestructura
                    sh "git clone https://github.com/anfedimo/kubernetes-u-sabana.git"
                    
                    dir('kubernetes-u-sabana') {
                        // Actualizar el tag de la imagen en values.yaml [cite: 2]
                        sh "sed -i 's/tag: .*/tag: \"${BUILD_NUMBER}\"/' charts/sabana-api/values.yaml"
                        
                        // Configurar git y subir cambios usando credenciales [cite: 3, 5]
                        withCredentials([usernamePassword(credentialsId: 'github-creds-sabana', 
                                                         usernameVariable: 'GIT_USER', 
                                                         passwordVariable: 'GIT_TOKEN')]) {
                            sh "git config user.email 'jenkins@sabana.edu.co'"
                            sh "git config user.name 'Jenkins Bot'" [cite: 4]
                            sh "git add charts/sabana-api/values.yaml"
                            sh "git commit -m 'GitOps: Update image to build ${BUILD_NUMBER}'"
                            sh "git push https://${GIT_TOKEN}@github.com/anfedimo/kubernetes-u-sabana.git main"
                        }
                    }
                }
            }
        }
    }
}