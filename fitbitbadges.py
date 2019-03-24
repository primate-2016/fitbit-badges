import logging
from fitbitbadgeclasses import FitBitBadgesUser, BadgesList

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    
    access_token = event['Records'][0]['accessToken']
    logger.info('access token is:{}'.format(access_token))
    output = access_token
    logger.info('returning output to web front-end \n:{}'.format(output))
    return output


if __name__ == '__main__':

    output = handler(None, None)