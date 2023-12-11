import os
import boto3
import mimetypes
from botocore.config import Config
import logging
logger=logging.getLogger()
logging.basicConfig(format='%(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')

def run():
    #for every env variable github actions will convert them into INPUT_(ENV VARIABLE in caps) example for env variable bucket it will be converted to INPUT_BUCKET
    bucket = os.environ['INPUT_BUCKET']
    bucket_region = os.environ['INPUT_BUCKET-REGION']
    dist_folder = os.environ['INPUT_DIST-FOLDER']

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.resource('s3', config=configuration)
    logger.info("S3 CLient")
    logger.info(s3_client)

    for root, subdirs, files in os.walk(dist_folder):
        for file in files:
            s3_client.upload_file(
                os.path.join(root, file),
                bucket,
                file
            )

    website_url = f'http://{bucket}.s3-website-{bucket_region}.amazonaws.com'
    # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'website-url={website_url}', file=gh_output)


if __name__ == '__main__':
    run()
