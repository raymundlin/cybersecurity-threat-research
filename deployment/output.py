import os
import json

if __name__ == '__main__':
  file_name = "out.json"
  file_path = os.path.join(os.path.dirname(__file__), file_name)

  if not os.path.isfile(file_path):
    print("File not found: {}".format(file_path))
    exit(1)
  
  # Read file
  with open(file_path, 'r') as f:
    data = json.load(f)

    stage = os.environ.get('CDK_DEPLOY_STAGE') or 'dev'

    # Print data
    print("Stage: {}".format(stage))
    print("Url: {}".format(data["DeploymentStack-{}".format(stage)]["url"]))