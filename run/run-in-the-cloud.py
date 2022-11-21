import boto3
import logging
from sagemaker.estimator import Estimator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Getting the AWS account id using STS
account_id = boto3.client('sts').get_caller_identity().get('Account')
#To-replace
#Replace with the region you're working in
region = "<your-region>"

#To-replace:
#Specify the IAM role you want your jobs to use
role = "<your-IAM-role>"
repository_name = "<repo-name>"
container_image_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{repository_name}:latest"


estimator = Estimator(
    entry_point="main.py",
    source_dir="../src/",  # directory of your training script
    role=role,
    image_uri=container_image_uri,
    train_instance_count=1,
    train_instance_type="ml.c5.xlarge", #we specify an instance type to run remotely on SageMaker
    hyperparameters={"my-variable": "my-variable-value"},
    base_job_name='sm-sample',
    disable_profiler=True
)

#To-replace
#Use your own datasets, these are just examples/placeholders
estimator.fit({"training":f"s3://sagemaker-{region}-{account_id}/data/fast-embedding/iris.csv",\
        "testing":f"s3://sagemaker-{region}-{account_id}/data/fast-embedding/iris.csv"},\
        wait=False)

console_link = f"https://{region}.console.aws.amazon.com/sagemaker/home?region={region}#/jobs/{estimator.latest_training_job.job_name}"
logger.info(f"Job is launched on AWS! Make sure you're loged in then go to SageMaker console or click here: {console_link}")