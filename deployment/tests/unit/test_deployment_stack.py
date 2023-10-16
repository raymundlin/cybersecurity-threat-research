import aws_cdk as core
import aws_cdk.assertions as assertions

from deployment.deployment_stack import DeploymentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in deployment/deployment_stack.py
def test_lambda_function_created():
    app = core.App()
    stack = DeploymentStack(app, "deployment", testing = True)
    template = assertions.Template.from_stack(stack)

    # Check Lambda Function Exists
    template.has_resource_properties("AWS::Lambda::Function", {
        "Handler": "list.main",
        "Runtime": "python3.9"
    })

def test_api_gateway_created():
    app = core.App()
    stack = DeploymentStack(app, "deployment", testing = True)
    template = assertions.Template.from_stack(stack)

    # Check API Gateway Exists
    template.has_resource_properties("AWS::ApiGateway::RestApi", {
        "Name": "Deployment Service",
    })
