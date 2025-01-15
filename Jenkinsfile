pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/futig/SimplePythonServer', branch: 'main')
      }
    }

    stage('Logs') {
      steps {
        sh '''ls -a
'''
      }
    }

  }
}