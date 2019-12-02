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
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh """
                        ls
                        pip install -r requirements.txt
                        python ./test.py
                        """
                    }
                }
            }
        }
        stage('Push logs') {
            steps {
                dir('/var/jenkins_home/workspace/automated_testing/python_tests'){
                    sh 'python push_test_logs.py'
                }
            }
        }
    }
}