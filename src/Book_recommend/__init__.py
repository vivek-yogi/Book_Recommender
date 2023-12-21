import os
import sys
import logging

logging_str  = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]" #[2023-11-04 00:01:44,730:INFO:test:Welome to our custom log]
log_dir      = "logs" # Directory name
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True) # Creating directory if not exist

logging.basicConfig( 
    level    = logging.INFO,
    format   = logging_str,
    handlers = [logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)] )

logger      = logging.getLogger("Book_recommend")  