import json
import datetime
import requests

def get_filtered_list(json_url, brand_filter=None):
    response = requests.get(json_url)
    json_data = json.loads(response.text)
    filtered_list = []
    for obj in json_data:
        if brand_filter is None or brand_filter in obj['brand']:
            obj_date = datetime.datetime.strptime(obj['date'], '%Y-%m-%d %H:%M:%S')
            if obj_date > datetime.datetime.now():
                filtered_list.append(obj)
    return filtered_list

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        if event['path'] == '/custom-warning':
            if 'web' in event['pathParameters'].values():
                json_url = 'https://www.example.com/web.json'
            elif 'app' in event['pathParameters'].values():
                json_url = 'https://www.example.com/app.json'
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Invalid parameter'})
                }
            filtered_list = get_filtered_list(json_url)
            return {
                'statusCode': 200,
                'body': json.dumps({'list': filtered_list})
            }
        elif event['path'] == '/brands':
            brand_filter = event['queryStringParameters'].get('brand')
            filtered_list = get_filtered_list('https://www.example.com/brands.json', brand_filter)
            return {
                'statusCode': 200,
                'body': json.dumps({'list': filtered_list})
            }
    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Resource not found'})
    }
