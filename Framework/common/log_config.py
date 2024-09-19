import logging
import os


def setup_logging(log_filename):
    log_path = os.path.join(os.getcwd(), 'Framework', 'Log')

    os.makedirs(log_path,exist_ok=True)

    log_file = os.path.join(log_path, log_filename)

    # config logging
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

