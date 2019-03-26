import boto3
import logging
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr # required for dynamodb queries

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class FitBitBadgesUser():
    """
    A class representing a user of the FitBitBadges app
    """

    def __init__(self, fitbit_user_id, dynamo_client, dynamo_table):
        self._fitbit_user_id = fitbit_user_id
        self._dynamo_client = dynamo_client
        self._dynamo_table = dynamo_table
    
    def check_if_user_exists(self):
        """
        Query dynamodb for the user id, return the list of badges
        if the user exists
        """
        table = self._dynamo_client.Table(self._dynamo_table)
        try:
            response = table.query(
                KeyConditionExpression=Key('UserID').eq(self._fitbit_user_id)
            )
        except ClientError as e:
            logger.error('Got an error from DynamoDB: {}'.format(e.response['Error']['Message']))
        if response['Items']:
            logger.info('Found Fitbit user {} in the database'.format(self._fitbit_user_id))
            return 'Yes'
        else:
            logger.info('Fitbit user {} was not found in the database'.format(self._fitbit_user_id))
            return 'No'

    def get_user(self):
        pass

    def create_user(self):
        pass

class BadgesList():
    """
    A class representing all the badges a user of the FitBitBadges app has earned
    """

    def __init__(self):
        pass
    
    def read_existing_badges(self):
        pass
    
    def find_new_badges(self):
        pass
    
    def write_new_badges(self):
        pass
    
