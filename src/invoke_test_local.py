from lambda_function import lambda_handler

payload = {
    'event': {
        'resource': '/custom-warning/{tipo}',
        'path': '/custom-warning/web',
        'httpMethod': 'GET',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'myapi.execute-api.us-east-1.amazonaws.com',
            'User-Agent': 'curl/7.64.1'
        },
        'queryStringParameters': None,
        'pathParameters': {
            'tipo': 'web'
        },
        'stageVariables': None,
        'requestContext': {
            'resourcePath': '/custom-warning/{tipo}',
            'httpMethod': 'GET',
            'path': '/prod/custom-warning/web',
            'protocol': 'HTTP/1.1',
            'requestTime': '17/May/2022:14:28:57 +0000',
            'requestTimeEpoch': 1652831337482,
            'requestId': 'abc123',
            'identity': {
                'cognitoIdentityPoolId': None,
                'accountId': None,
                'cognitoIdentityId': None,
                'caller': None,
                'sourceIp': '192.0.2.1',
                'principalOrgId': None,
                'accessKey': None,
                'cognitoAuthenticationType': None,
                'cognitoAuthenticationProvider': None,
                'userArn': None,
                'userAgent': 'curl/7.64.1',
                'user': None
            },
            'pathParameters': {
                'tipo': 'web'
            },
            'resourceId': 'xyz123',
            'stage': 'prod'
        },
        'body': None,
        'isBase64Encoded': False
    },
    'context': {}
}

context = {
    'function_name': 'my-lambda-function',
    'function_version': '1.0',
    'invoked_function_arn': 'arn:aws:lambda:us-east-1:123456789012:function:my-lambda-function',
    'memory_limit_in_mb': 256,
    'aws_request_id': 'abc123',
    'log_group_name': 'my-lambda-function-log-group',
    'log_stream_name': 'my-lambda-function-log-stream',
    'identity': None,
    'client_context': None,
    'remaining_time_in_millis': 1000
}

lambda_handler(payload, context)