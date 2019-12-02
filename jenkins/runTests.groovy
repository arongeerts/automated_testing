pipeline {
    agent any
    stages {
        stage('Get source code') {
            steps {
                dir('/var/jenkins_home/automated_testing'){
                    sh """
                    git clone https://github.com/arongeerts/automated_testing.git
                    """
                }
            }
        }
        stage('Test') {
            steps {
                dir('/var/jenkins_home/automated_testing/python_code'){
                    sh 'python ./test.py'
                }
            }
        }
        stage('Push logs') {
            steps {
                dir('/var/jenkins_home/automated_testing/python_code'){
                    sh 'python push_test_logs.py'
                }
            }
        }
    }
}