from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split
import os
from get_param import get_param
from argparse import ArgumentParser
import pandas as pd
def split_data(config_path):
    config=get_param(config_path)
    data_path=config['load_data']['raw']
    df=pd.read_csv(data_path)
    train_=config['split']['train']
    test_=config['split']['test']
    train,test=train_test_split(df,test_size=.25,random_state=0)
    train.to_csv(train_,sep=',',encoding='utf8',index=False)
    test.to_csv(test_,sep=',',encoding='utf8',index=False)

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed=arg.parse_args()
    split_data(parsed.config)

    # train_path=config['process_and_load']['train']
    # test_path=config['process_and_load']['test']