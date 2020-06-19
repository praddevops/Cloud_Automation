"""
this python scripts reads ec2 configuration from an yaml file (default: ec2.yaml in current directory) and creates ec2 instance
required 3rd party packages: boto3, pyyaml
"""

import boto3
import boto3.session
import yaml

ec2_config_file = 'ec2.yaml'

with open(ec2_config_file, "r") as file:
    ec2_config = yaml.load(file, Loader=yaml.FullLoader)

session = boto3.session.Session()

ec2 = session.resource('ec2', region_name="us-east-1")

volumedevices = []

for i in ec2_config['server']['volumes']:
    
        volumedevices.append({
                    'DeviceName': i['device'],
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': i['size_gb'],
                        'VolumeType': i['type'],
                        'Encrypted': True
                    },
                })

publickey_bytes = str.encode(ec2_config['server']['users'][0]['ssh_key'])

upload_public_key = ec2.import_key_pair(
    DryRun=False,
    KeyName='mykeypair123',
    PublicKeyMaterial=publickey_bytes,
)

# create a new EC2 instance
instances = ec2.create_instances(
     BlockDeviceMappings=volumedevices,
     ImageId=ec2_config['server']['image_id'],
     MinCount=1,
     MaxCount=1,
     InstanceType=ec2_config['server']['instance_type'],
     DryRun=False,
     KeyName='mykeypair123'
 )
