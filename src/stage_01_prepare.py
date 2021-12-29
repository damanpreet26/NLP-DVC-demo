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
    artifacts=config["artifacts"]
    create_dir([os.path.join(artifacts["artifacts_dir"],artifacts["prepared_data_dir"])])

    train_data_path=os.path.join(artifacts["artifacts_dir"],artifacts["prepared_data_dir"],artifacts["train_data"])
    test_data_path=os.path.join(artifacts["artifacts_dir"],artifacts["prepared_data_dir"],artifacts["test_data"])

    print(train_data_path)
    print(test_data_path)
    print(input_data)

    encode="utf8"
    with open(input_data, "r", encoding=encode) as data_file:
        with open(train_data_path,"w", encoding=encode) as train_file:
            with open(test_data_path,"w",encoding=encode) as test_file:
                pass
                #process_post(data_file, train_file, test_file,"<python>",split)
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
