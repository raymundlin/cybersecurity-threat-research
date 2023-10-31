import os
import json
from package import yaml
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_file(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        logger.error("File not found")
        return None
    
    # Check if file is a YAML file
    if not (file_path.endswith('.yaml') or file_path.endswith('.yml')):
        logger.warning("File is not a YAML file")
        return None
    
    # Read YAML file
    with open(file_path, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
            return file
        except yaml.YAMLError as exc:
            logger.fatal("Error while reading YAML file")
            return None
    

def main(event, lambda_context):
    """Main function."""
    logger.debug(event)

    file_path = event["path"]
    file_path = file_path.replace("/", "", 1)

    logger.info("Start Get Item from {}".format(file_path))

    file = get_file(file_path)
    if file == None:
      return {
          'statusCode': 404,
          'body': json.dumps({
              "message": "File not found",
          })
      }
    else:
      return {
        'statusCode': 200,
        'body': json.dumps(file),
      }