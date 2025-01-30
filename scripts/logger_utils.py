import logging
import sys,os
# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self._setup_handlers()

    def _setup_handlers(self):
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # File handler using config
        file_handler = logging.FileHandler(config.LOG_FILE)
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

# Example of how to use it
# if __name__ == '__main__':
#     # Assuming your config.py has a LOG_FILE variable
#     logger_instance = Logger("my_app")
#     logger = logger_instance.get_logger()

#     logger.info("This is a test message.")
#     logger.warning("This is a warning message")
#     logger.error("This is an error message")
