import pandas as pd
import yaml
import os


def read_yaml(file_path:str)->dict:
    with open(file_path) as file:
        content=yaml.safe_load(file)
    return content

def create_dir(dirs: list):
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
    print(f"Directory created at {dir}")
