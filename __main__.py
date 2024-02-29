"""An AWS Python Pulumi program"""

from infra.lambdas import *

import pulumi

pulumi.export("apigatewayv2-http-endpoint", pulumi.Output.all(http_endpoint.api_endpoint, http_stage.name).apply(lambda values: values[0] + '/' + values[1] + '/'))
