import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import re

def process_post(data_file, train_file, test_file,target_tag,split):
    line_nu=1
    for line in tqdm(data_file):
        try:
            fd_out= train_file if random.random()>split else test_file
            attr=ET.fromstring(line).attrib

            pid=attr.get("Id","")
            label= 1 if target_tag in attr.get("Tags","") else 0
            title = re.sub(r"\s+"," ", attr.get("Title","")).strip()
            body= re.sub(r"\s+"," ", attr.get("Body","")).strip()
            text= title+" "+body

            fd_out.write(f"{pid}\t{label}\t{text}\n")
            line_nu+=1
        except Exception as e:
            msg=f"Thre was a exception at {line_nu} at {e}\n"
            logging.exception(msg)


