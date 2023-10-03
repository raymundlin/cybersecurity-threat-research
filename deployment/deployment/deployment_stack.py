from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway,
)
from constructs import Construct

class DeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, testing: bool = False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        source_code = _lambda.Code.from_asset("./deployment/app") if testing else _lambda.Code.from_asset("./app")

        list_func = _lambda.Function(
            self, "list-api",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=source_code,
            handler="list.main",
            timeout=Duration.seconds(10),
        )

        api = api_gateway.RestApi(
            self, 'deployment-api',
            rest_api_name='Deployment Service',
            description='This service serves deployment.',
            deploy_options=api_gateway.StageOptions(
                stage_name='prod',
            )
        )

        api.root.add_method(
            'GET', api_gateway.LambdaIntegration(
                list_func, proxy=True,
            ),
        )
