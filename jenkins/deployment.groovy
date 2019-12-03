pipeline {
    agent any
    stages {
        stage('Get source code') {
            steps {
                dir('/var/jenkins_home/workspace'){
                    sh """
                    rm -rf automated_testing || true
                    git clone https://github.com/arongeerts/automated_testing.git
                    """
                }
            }
        }
        stage('Test') {
            steps {
                dir('/var/jenkins_home/workspace/automated_testing/python_tests') {
                    sh """
                    python ./unit_test.py
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo do deployment'
            }
        }
    }
}