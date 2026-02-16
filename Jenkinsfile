stage('GitOps Sync Notification') {
    steps {
        container('docker') {
            // Clonar repo de infraestructura
            sh "git clone https://github.com/anfedimo/kubernetes-u-sabana.git"
            dir('kubernetes-u-sabana') {
                // Actualizar el tag de la imagen en values.yaml usando yq o sed
                sh "sed -i 's/tag: .*/tag: \"${BUILD_NUMBER}\"/' charts/sabana-api/values.yaml"
                
                // Configurar git y subir cambios
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