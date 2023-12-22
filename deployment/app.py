#!/usr/bin/env python3
import os
import shutil

import aws_cdk as cdk
from deployment.deployment_stack import DeploymentStack
import os

FOLDERS = ["threat", "domain"]

# Remove app folder assets
# Copy folders to app folder
for folder in FOLDERS:
    if os.path.isdir("./app/{}".format(folder)):
      shutil.rmtree("./app/{}".format(folder))
    shutil.copytree("../{}".format(folder), "./app/{}".format(folder))

env = cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"])
stage = os.environ.get('CDK_DEPLOY_STAGE') or 'dev'
Osaka = cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="ap-northeast-3")

app = cdk.App()
DeploymentStack(app, "DeploymentStack", env=Osaka)

app.synth()
