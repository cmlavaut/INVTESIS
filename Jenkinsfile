#!groovy
pipeline {
   agent any
   stages {
    stage('Construir imagen Docker') {
            steps {
                script {
                    // Construye la imagen Docker usando el Dockerfile
                    sh 'docker build -t kmilavaut/testapp -f flask/Dockerfile flask'
                    }
                }
    }
    stage('Ejecutar imagen Docker') {
            steps {
                script {
                    // Ejecuta un contenedor a partir de la imagen Docker
                    sh 'docker run --rm kmilavaut/testapp'
                }
            }
        }
    }
     post {
        always {
            echo 'Pipeline completo.'
        }
        success {
            echo 'Pipeline finalizado con éxito.'
        }
        failure {
            echo 'El pipeline falló.'
        }
    }
}
