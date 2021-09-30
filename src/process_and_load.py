import yaml
import pandas as pd
from argparse import ArgumentParser
from get_param import get_data,get_param
from sklearn.impute import SimpleImputer
import numpy as np
def process_load(config_path):
    config=get_param(config_path)
    df=get_data(config_path)
    col=df.columns
    si=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
    df=si.fit_transform(df)
    df=pd.DataFrame(df,columns=col)
    raw=config['load_data']['raw']
    df.to_csv(raw,sep=',',encoding='utf8',index=False)

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed=arg.parse_args()
    process_load(parsed.config)
