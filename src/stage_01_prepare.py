import yaml
import argparse
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

def main():
    print("one")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config)","-c",default="config/config.yaml")
    parsed_Args=args.parse_args()
    try:
        logging.info("\n **************")
        logging.info(">>>>>Stage<<<<<<")
        main()
        logging.info("Stage 01, complete")
    except Exception as e:
        logging.exception(e)
        raise e
