import os
import sys
import logging
from rich.logging import RichHandler

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
if not os.path.exists(os.path.join(log_dir,"running_logs.log")):
    with open (os.path.join(log_dir,"running_logs.log"),'w'):
        pass 
log_filepath = os.path.join(log_dir,"running_logs.log")


logging.basicConfig(
    # level= logging.INFO,
    level="NOTSET",
    format= logging_str,

    handlers=[
        RichHandler(),
        logging.FileHandler(log_filepath),
        # logging.StreamHandler(sys.stdout),
        
    ]
)

log = logging.getLogger("mlapp")