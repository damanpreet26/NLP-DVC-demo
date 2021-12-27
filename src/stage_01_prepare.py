import Pyyaml
import argparse
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

def main(config, params):
    conf=read_yaml(config)
    param=read_yaml(params)

    source_data=conf["source_data"]
    input_data=os.path.join(source_data["data_dir"],source_data["data_file"])

    split = param["prepare"]["split"]
    seed = param["prepare"]["seed"]
    random.seed(Seed)

    artifacts=conf["artifacts"]
    prepared_data_path=os.path.join(artifacts["artifacts"],artifacts["prepared_data_dir"])




    print("one")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config)","-c",default="config/config.yaml")
    args.add_argument("--params)", "-p", default="params.yaml")
    parsed_Args=args.parse_args()
    try:
        logging.info("\n **************")
        logging.info(">>>>>Stage<<<<<<")
        main(config=parsed_Args.config, params=parsed_Args.params)
        logging.info("Stage 01, complete")
    except Exception as e:
        logging.exception(e)
        raise e
