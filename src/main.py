import os
import time
import argparse
import logging
import helpers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--my-variable", type=str, default="my-default-variable-value")
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAINING"])
    parser.add_argument("--test", type=str, default=os.environ["SM_CHANNEL_TESTING"])

    args, _ = parser.parse_known_args()

    return args

def train(args):
    """
    Your training function
    Args: All the argument passed in estimator.fit(hyperparameters=arg_dict).
          These are passed during training execution as command line arguments
    """
    
    #<channel-name> is what you specify when you call estimator.fit(inputs={"<channel-name>":"path-to-s3"})
    #On runtime this is copied to "/opt/ml/input/data/<channel-name>" which is also the default value for os.environ["SM_CHANNEL_<channel-name>"]
    #More info here : https://github.com/aws/sagemaker-training-toolkit/blob/master/ENVIRONMENT_VARIABLES.md
    train_path = args.train
    test_path = args.test
    
    #To-complete
    #Add code that reads data from the local path


    #To-complete
    #Replace with your training code
    logger.info("Launching execution of code")
    start_time = time.time()

    #Anything you print following the regex rules in estimator.fit(metric_definitions=[{"Name":"<metric_name>":"Regex":"<Regex_rule>"}])
    #will be parsed by SageMaker and shown as algorithm metrics
    for i in range(4):
        time.sleep(2)
        logger.info(f"Train_metric={i};")

    #Demonstrating you can call external functions within your repository
    #Everything in the "source_dir" (specified when you create the estimator) is accessible during training
    helpers.function_from_helpers()

    end_time = time.time()
    logger.info(f"Execution took  {end_time-start_time}")

    
    #To-complete
    #save your model artifact to "os.environ["SM_MODEL_DIR"]"
    #It will be packaged and saved back to S3
    logger.info(f"Just saved model to {os.environ['SM_MODEL_DIR']}")
    
    logger.info("SUCCESS - Done executing the main script")

if __name__ == "__main__":
    args = parse_args()
    logger.info(f"Arguments parsed from SageMaker: {args}")
    logger.info("Launching training job")
    train(args)
    logger.info("Finished calling the main file")

