# automated_testing
An example of automated testing for SQL databases using Python

## How to use
```docker-compose up``` will launch the following services:<br>
* Jenkins at ```http://localhost:10001```
* Localstack S3 mockup at ```http://localhost:5002```
* A mysql database with DDL as defined in db/initdb.sql

## Configuring Jenkins
In the terminal where you executed the ```docker-compose``` statement, 
Jenkins will print an initial Admin password. This has to be copy pasted
the first time you navigate to ```localhost:10001```

Next, create two pipelines, configured to use a script from SCM, 
pointing to the code from jenkins/deployment.groovy 
and jenkins/scheduled_tests.groovy. For the deployment pipeline, you can add a
trigger to poll SCM with schedule '* * * * *'. 
This will trigger the pipeline on every commit to master 