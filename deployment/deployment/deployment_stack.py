from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway,
    CfnOutput,
)
from constructs import Construct

class DeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, stage: str = 'prod', testing: bool = False, **kwargs) -> None:
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

        get_item_func = _lambda.Function(
            self, "get-item-api",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("./deployment/app") if testing else _lambda.Code.from_asset("./app"),
            handler="item.main",
            timeout=Duration.seconds(10),
        )

        api = api_gateway.RestApi(
            self, 'deployment-api',
            rest_api_name='Deployment Service',
            description='This service serves deployment.',
            deploy_options=api_gateway.StageOptions(
                stage_name=stage,
            ),
        )

        api.root.add_method(
            'GET', api_gateway.LambdaIntegration(
                list_func, proxy=True,
            ),
            method_responses=[api_gateway.MethodResponse(
                status_code='200',
            )],
        )
        
        api_domain = api.root.add_resource("domain")
        api_domain_study = api_domain.add_resource("study")

        domain_study = api_domain_study.add_resource('{item}')
        domain_study.add_method(
            'GET', api_gateway.LambdaIntegration(
                get_item_func, proxy=True,
            ),
            method_responses=[api_gateway.MethodResponse(
                status_code='200',
            )],
        )
        
        # Output to CfnOutput
        CfnOutput(self, "url", value=api.url)
