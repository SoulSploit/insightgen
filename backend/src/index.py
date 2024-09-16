import json
import os
import boto3
import logging
import time
from botocore.exceptions import ClientError

# Initialize DynamoDB resource and logger
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables for configuration
MAX_ITEMS = int(os.environ.get('MAX_ITEMS', 1000))  # Max number of items to retrieve
if MAX_ITEMS <= 0:
    raise ValueError("MAX_ITEMS must be a positive integer.")

PROJECTION_EXPRESSION = os.environ.get('PROJECTION_EXPRESSION', None)  # Optional attribute projection

def scan_table(scan_kwargs):
    """Perform a scan operation with retries and exponential backoff."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = table.scan(**scan_kwargs)
            if 'Items' not in response:
                logger.warning(f"No items returned from scan. Scan kwargs: {scan_kwargs}")
            return response
        except ClientError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                logger.warning(f"Retrying scan operation: attempt {attempt + 1}. Error: {e}. Waiting {wait_time} seconds.")
                time.sleep(wait_time)
            else:
                logger.error(f"Scan operation failed after {max_retries} attempts. Error: {e}")
                raise
        except Exception as e:
            logger.error(f"Unexpected error during scan operation: {str(e)}")
            raise

def handler(event, context):
    """
    Lambda function handler to scan DynamoDB table and return results.
    
    Args:
        event (dict): The event data passed to the function.
        context (object): The runtime information of the Lambda function.
    
    Returns:
        dict: A response object with status code, body, and headers.
    """
    scan_kwargs = {}
    if PROJECTION_EXPRESSION:
        scan_kwargs['ProjectionExpression'] = PROJECTION_EXPRESSION
    
    data = []
    last_evaluated_key = None
    
    try:
        while True:
            if last_evaluated_key:
                scan_kwargs['ExclusiveStartKey'] = last_evaluated_key
            
            response = scan_table(scan_kwargs)
            items = response.get('Items', [])
            if not items:
                logger.info("No more items to retrieve.")
                break
            
            data.extend(items)
            
            if len(data) >= MAX_ITEMS or 'LastEvaluatedKey' not in response:
                break
            
            last_evaluated_key = response['LastEvaluatedKey']
        
        # Trim data to MAX_ITEMS if necessary
        data = data[:MAX_ITEMS]
        
        return {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except ClientError as e:
        logger.error(f"ClientError: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
