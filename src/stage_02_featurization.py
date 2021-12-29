import argparse
import random
from src.utils.data_mgmt import process_post
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

def featurization(config_path, params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    artifacts=config["artifacts"]
    feature=config["feature_data_dir"]

    train_data_path=os.path.join(artifacts["artifacts_dir"],artifacts["prepared_data_dir"],artifacts["train_data"])
    test_data_path=os.path.join(artifacts["artifacts_dir"],artifacts["prepared_data_dir"],artifacts["test_data"])

    train_feat_path=os.path.join(artifacts["artifacts_dir"],artifacts["feature_data_dir"],artifacts["feature_train_file"])
    test_feat_path=os.path.join(artifacts["artifacts_dir"],artifacts["feature_data_dir"],artifacts["feature_testfile"])


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","--c",default="config/config.yaml")
    args.add_argument("--params", "--p", default="params.yaml")
    parsed_Args=args.parse_args()
    try:
        logging.info("\n **************")
        logging.info(">>>>>Stage<<<<<<")
        featurization(config_path=parsed_Args.config, params_path=parsed_Args.params)
        logging.info("Stage 01, complete")
    except Exception as e:
        logging.exception(e)
        raise e
