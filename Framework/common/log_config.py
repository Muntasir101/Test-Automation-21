import logging
import os


def setup_logging(log_filename='Framework/Log/test_log.log'):
    log_path = os.path.join(os.getcwd(), 'Framework', 'Log')

    log_file = os.path.join(log_path, 'log_filename')

    # config logging
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Logging Setup Complete")
