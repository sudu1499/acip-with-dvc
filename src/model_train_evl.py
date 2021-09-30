from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from get_param import get_param
from argparse import ArgumentParser
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import pickle as pk
import os
import json
def metrics(ypred,ytest):
    score=accuracy_score(ytest,ypred)
    print('accuracy score for knn model ',score)
    return score
def model(config_path):
    config=get_param(config_path)
    train_=config['split']['train']
    test_=config['split']['test']
    n=config['model']['knn']['params']['n_neighbours']
    train=pd.read_csv(train_)
    test=pd.read_csv(test_)
    xtrain=train.iloc[:,[0,1,4,6,10,11,12]].values
    ytrain=train['salary'].values
    xtest=test.iloc[:,[0,1,4,6,10,11,12]].values    
    ytest=test['salary'].values

    le=LabelEncoder()
    ytrain=le.fit_transform(ytrain)

    le=LabelEncoder()
    ytest=le.fit_transform(ytest)
    
    ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1,3])],remainder='passthrough')
    ct.fit(xtrain)
    xtrain=ct.transform(xtrain).toarray()

    xtest=ct.fit_transform(xtest).toarray()

    knn=KNeighborsClassifier(n_neighbors=n)
    knn.fit(xtrain,ytrain)

    ypred=knn.predict(xtest)

    score=metrics(ypred,ytest)
    model_=config['saved_model']

    pk.dump(knn,open(os.path.join(model_,'knnmodel.pkl'),'wb'))
    pk.dump(ct,open(os.path.join(model_,'ct.pkl'),'wb'))

    param_=config['report']['params']
    scores_=config['report']['metrics']

    with open(param_,'w') as f:
        t=json.dumps(config['model']['knn']['params'])
        f.write(t)

    with open(scores_,'w') as f:
        t=json.dumps({'accuracy':score})
        f.write(t)

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed=arg.parse_args()
    model(parsed.config)
    
