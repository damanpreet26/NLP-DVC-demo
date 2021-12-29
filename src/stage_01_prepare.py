import argparse
import random

from src.utils.all_utils import  *
import os
import shutil
from tqdm import tqdm
import logging

logging.basicConfig(
    filename=os.path.join("logs","running.logs"),
    level=logging.INFO,
    filemode="a",
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
)

def main(config_path, params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    source_data=config["source_data"]
    input_data=os.path.join(source_data["data_dir"],source_data["data_file"])
    #print(input_data)

    split = params["prepare"]["split"]
    seed_val = params["prepare"]["seed"]
    random.seed(seed_val)
    #print(seed_val)
    print(os.path.join(config["artifacts"]["artifacts_dir"],config["artifacts"]["prepared_data_dir"]))
    create_dir([os.path.join(config["artifacts"]["artifacts_dir"],config["artifacts"]["prepared_data_dir"])])

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","--c",default="config/config.yaml")
    args.add_argument("--params", "--p", default="params.yaml")
    parsed_Args=args.parse_args()
    try:
        logging.info("\n **************")
        logging.info(">>>>>Stage<<<<<<")
        main(config_path=parsed_Args.config, params_path=parsed_Args.params)
        logging.info("Stage 01, complete")
    except Exception as e:
        logging.exception(e)
        raise e
