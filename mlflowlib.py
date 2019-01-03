''' This library is dedicated to integration to MLflow'''

import mlflow
import datetime

def log_data(expName, paramDict, metricDict):
    
    mlflow.set_experiment(expName)
    
    with mlflow.start_run():    
    
        for (key,value) in paramDict.items():
            mlflow.log_param(key,value)

        for (key,value) in metricDict.items():
            mlflow.log_metric(key,value)
        
        print("Data successfully logged to experiment " + expName)


def log_file(expName, fileVersion, fileName):
    
    mlflow.set_experiment(expName)
    
    with mlflow.start_run():
        #print(datetime.datetime.now())
        mlflow.log_param('Date-time',datetime.datetime.now())
        mlflow.log_param('Version', fileVersion)
        mlflow.log_param('Filename', fileName)
        
        print("Data successfully logged to experiment " + expName)

