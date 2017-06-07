pipeline {
    agent { docker 'python:3.6.1' }
    stages {
        stage('clone') {
            steps {
                git 'https://github.com/yehudash/SCE-Tirgul-2'
            }
        }
    }
}
