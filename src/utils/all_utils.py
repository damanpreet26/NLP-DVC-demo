import pandas as pd
import yaml
import os


def read_yaml(file_path:string)->dict:
    with open(file_path) as file:
        content=yaml.safe_load(file)
    return content
