pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
                git 'https://github.com/yehudash/SCE-Tirgul-2'
            }
        }
        stage('Execute unit tests') {
            steps {
                sh 'nosetests --with-xunit'
            }
        }

    }
}
