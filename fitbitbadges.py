import logging
import sys
import boto3
from fitbitbadgeclasses import FitBitBadgesUser, BadgesList

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    
    # Does this look anything  like the exected event? If not bail immediately.
    if 'Records' not in event:
        logger.error('Records list not found in event, bailing')
        sys.exit(0)
    if 'accessToken' not in event['Records'][0]:
        logger.error('no access token found in event, bailing')
        sys.exit(0)

    fitbit_user_id = event['Records'][0]['accountUserId']
    # instantiate a DynamoDB client object - user a resource object
    # rather than a client because I am going to pass it around a lot
    dynamo_client = boto3.resource('dynamodb')
    # instantiate user class
    dynamo_table = 'wibble'
    badges_user = FitBitBadgesUser(fitbit_user_id, dynamo_client, dynamo_table)

    # query db to see if user exists

    # if not get user full name and get list of badges

    # if exists, get current list of badges

    # if exists, get list of badges

    # if exists, compare old to new

    # return list of new badges to web app
    access_token = event['Records'][0]['accessToken']
    logger.info('access token is:{}'.format(access_token))
    output = access_token
    logger.info('returning output to web front-end \n:{}'.format(output))
    return output


if __name__ == '__main__':

    output = handler(None, None)