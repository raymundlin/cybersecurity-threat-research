import os
import shutil
import aws_cdk as cdk
from deployment.deployment_stack import DeploymentStack
FOLDERS = ["threat", "domain"]
# Remove app folder assets
# Copy folders to app folder
for folder in FOLDERS:
    if os.path.isdir("./app/{}".format(folder)):
      shutil.rmtree("./app/{}".format(folder))
    shutil.copytree("../{}".format(folder), "./app/{}".format(folder))
Osaka = cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="ap-northeast-3")

app = cdk.App()
DeploymentStack(app, "DeploymentStack", env=Osaka)
DeploymentStack(app, "DeploymentStack-B11009049", env=Osaka)

app.synth()