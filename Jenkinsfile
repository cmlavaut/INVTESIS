#!groovy
pipeline {
    agent none
   stages {     
    stage('Docker BUILD') {
      agent any {         
       steps {
        sh 'docker build -t kmilavaut/testapp -f flask/Dockerfile flask'
      }
    }
  }
}
}