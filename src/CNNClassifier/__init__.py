import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir , "running_logs.log")
os.makedirs(log_dir , exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        
    ]
)



        # handlers = [ ... ]:
        # This line defines a list of logging handlers. Handlers determine where the log messages should be sent. In this case, it specifies two handlers within a list:

        # a. logging.FileHandler(log_filepath):
        # This creates a FileHandler instance and specifies log_filepath as the file where log messages should be written. The FileHandler sends log messages to a file.

        # b. logging.StreamHandler(sys.stdout):
        # This creates a StreamHandler instance and specifies sys.stdout as the stream where log messages should be written. sys.stdout represents the standard output, so log messages will also be printed to the console.
        

logger = logging.getLogger("cnnclassifierLogger")