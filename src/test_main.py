import os
import logging
from argparse import Namespace
from main import train

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Env:
    def __init__(self):
        # Helps simulate container environement variables
        # when sagemaker launchs a training job it makes uses of environment variables
        # for more details you can see https://github.com/aws/sagemaker-training-toolkit/blob/master/ENVIRONMENT_VARIABLES.md
        # we use this class to replicate that environment locally
        os.environ["SM_CHANNEL_TRAINING"] = "/tmp/data"
        os.environ["SM_CHANNEL_TESTING"] = "/tmp/data"
        os.environ["SM_MODEL_DIR"] = "/tmp/model/"

if __name__ == "__main__":
    #sets up the envitonment variables done by SageMaker automatically
    Env()

    #hard code hyperparameter for testing without changing structure of train function
    #uses Namespace and a dictionary to emulate same behavior as argumentparser
    param_dict = {"train":os.environ['SM_CHANNEL_TRAINING'],
                  "test":os.environ['SM_CHANNEL_TESTING'],
                  "my-variable":"my-variable-value-2"}

    args = Namespace(**param_dict)

    logger.info(f"Arguments parsed from SageMaker: {args}")
    train(args)
    logger.info("Finished testing training")
