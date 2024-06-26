# read the parameters
# process
# copy the data to raw dir /  retrun data frame

import os
import yaml
import pandas as pd
import argparse

# 3. define read_params function we are referring in # 2
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# 2 . create get_data function

def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    #print(df.head())
    return df

# extra comments
    

# 1.create name as an entry point
if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data= get_data(config_path=parsed_args.config)

