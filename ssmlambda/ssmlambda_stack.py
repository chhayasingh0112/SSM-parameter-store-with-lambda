from aws_cdk import (
    # Duration,
    aws_lambda as _lambda,

    aws_ssm as ssm,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from aws_solutions_constructs import (
    aws_lambda_ssmstringparameter as lambdassm

)

class SsmlambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        lambdassm.LambdaToSsmstringparameter(
            self, 'test-lambda-ssmstringparameter-stack',
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset('lambda'),
                runtime=_lambda.Runtime.PYTHON_3_10,
                handler='index.handler'
            ),
            string_parameter_props=ssm.StringParameterProps(
                string_value="test-string-value")
        )

        # The code that defines your stack goes here
        
        # example resource
        # queue = sqs.Queue(
        #     self, "SsmlambdaQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
