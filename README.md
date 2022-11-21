## A lift and shift approach for getting started with Amazon SageMaker

<em>How to run your code on Amazon SageMaker with as little change as possible.</em>

![intro-image](https://github.com/aws-samples/amazon-sagemaker-lift-and-shift/blob/main/intro-image.png?raw=true)

If you considered building new ML projects on Amazon Web Services (AWS) cloud or migrating existing ones you probably heard about [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html). It’s a fully managed machine learning service that enables data scientists and developers to build, train and deploy their Machine Learning models in the AWS cloud. The "lift and shift" approach consists of moving an application from one environment to another without re-designing the code's logic.

We aim to strike a balance between simplicity and completeness of functionality, so we provide an entry point for data scientists who want to utilize SageMaker for their existing AI/ML projects, making as few changes as possible to the codebase while also taking advantage of SageMaker built-in functionalities. In particular, we focus on cases where scripts are heavily used (vs notebooks), a simple docker container that you control (not AWS managed) is used to package the code, and where the main goal is to run your code at scale and in a secure managed environment.

If you are however, instead, interested in diving deep into specific service functionalities, I recommend checking the official [SageMaker documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html). You can also browse the vast and rich code examples in the [amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples) repository for code samples.

### Sidenote on the MLOps aspect of this template

This template, even though minimalistic and simple, consists of a strong training MLOps baseline. In one git repository template, we handle versioning of scientific, data, and infrastructure code, with cloud orchestration (SageMaker Training) that decouples persistent development and ephemeral compute environments.

Additionally, as each training job persists meta-data about training data, hyperparameters, metrics, and artifacts produced, we end up with a decent experiment management framework. Finally, depending on the complexity of the use case, we might require a graph of compute tasks, which can easily be done with Airflow, AWS StepFunctions, SageMaker pipelines, etc.

## How-to.

1.  Set up your environment

        $conda create -n myenv python=3.7.11
        $conda activate myenv
        $pip install -r src/requirements.txt

2.  Add your code and update the src/main.py (look for places in the file with "To-complete")

3.  [optional] Test the code locally

    When packaging your train.py to work with SageMaker you changed the code to read from certain environement variables. If you're not statisifed with the local mode of SageMaker (explained below) you can test your code in similar conditions using the following file:

        $python src/test_main.py

4.  Build a custom docker image using the Dockerfile and build_and_push.sh script:

    Make sure docker is running and run:

        $sh build_and_push.sh <AWS-ACCOUNT-NUMBER> <AWS-REGION> <NAME-OF-ECR-REPO>

5.  Update the **run/run-in-the-cloud.py** and **run/run-using-local-mode.py** with the right IAM role and ECR repository name

    - IAM role: Make sure the role you're using has sufficient permissions. If you're unsure you can start with AmazonSageMakerFullAccess ([documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonSageMakerFullAccess) and [IAM policy](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess$jsonEditor)) for demo purposes.
    - ECR repository name: The same value you used in step 4.

6.  Run a training job in SageMaker

    ->Local mode: This allows you run a SageMaker training job but locally.

        $cd run
        $python run-using-local-mode.py

    ->Standard mode: This triggers the execution of a SageMaker training job on your AWS account.

        $cd run
        $python run-in-the-cloud.py

    You can directly access your training job from the hyperlink in the logs !

## FAQ

**Q: Where can I run the code of thiss repository?**  
A: Anywhere you like. As long as you have the required libraries installed and are authentificated to your AWS account with the right permissions to make S3, ECR and SageMaker API calls, you're good to do.

**Q: Why is there placeholders and 'To-complete' comments everywhere?**  
A: The purpose of the template is to demonstrate key functionalities you might need when moving your code to SageMaker. Adding 'MNIST' like examples might create additional friction to the main purpose of "Making your code run (whatever it is) in SageMaker"

**Q: What's the difference between test_main.py and run-using-local-mode.py ?**  
A: SageMaker uses environment variables and command line parameters to communicate information to your script (data location, hyperparameters, etc.).

<em>run-using-local-mode.py</em> is the easiest way to test locally as SageMaker takes care of pulling the docker image, setting the environment variables and runs your script.

In certain cases you don't want an end-to-end execution of your script (testing line by line for example). <em>test_main.py</em> offers that experience as it sets the environment variables for you and passes the hyperparameters as a python dictionnary instead.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
