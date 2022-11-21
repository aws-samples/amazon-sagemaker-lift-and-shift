ACCOUNT_ID=$1
REGION=$2
ECR_REPO_NAME=$3

docker build -t $ECR_REPO_NAME .

docker tag $ECR_REPO_NAME $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$ECR_REPO_NAME:latest


# If the repository doesn't exist in ECR, create it.

aws ecr describe-repositories --repository-names "${ECR_REPO_NAME}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${ECR_REPO_NAME}" > /dev/null
fi

# Get the login command from ECR and execute it directly
aws ecr get-login-password --region "${REGION}" | docker login --username AWS --password-stdin "${ACCOUNT_ID}".dkr.ecr."${REGION}".amazonaws.com

docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$ECR_REPO_NAME:latest