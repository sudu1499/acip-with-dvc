from typing import DefaultDict
import yaml
import pandas as pd
from argparse import ArgumentParser
def get_param(config_path):
    with open(config_path) as f:
        config=yaml.safe_load(f)
    return config

def get_data(config_path):
    config=get_param(config_path)
    data_path=config['data_source']
    df=pd.read_csv(data_path)
    return df
if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='params.yaml')
    parsed=arg.parse_args()
    config=get_param(parsed.config)