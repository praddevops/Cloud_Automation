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

ec2 = session.resource('ec2')

volumedevices = []
user_data = ["#!/bin/sh\n"]

for i in ec2_config['server']['volumes']:
    
        volumedevices.append({
                    'DeviceName': i['device'],
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': i['size_gb'],
                        'VolumeType': i['volume_class'],
                        'Encrypted': True
                    },
                })
        if i['mount'] != "/":
            user_data.append("sudo mkfs -t "+i['type']+" "+i['device']+"\n"+"sudo mkdir -p "+i['mount']+"\n"+"sudo mount "+i['device']+" "+i['mount'])

publickey_bytes = str.encode(ec2_config['server']['users'][0]['ssh_key'])
user_data_string = ''.join(user_data)

user_data_string_b64 = str.encode(user_data_string)

upload_public_key = ec2.import_key_pair(
    DryRun=False,
    KeyName='mykeypair123',
    PublicKeyMaterial=publickey_bytes,
)




# create a new EC2 instance
instances = ec2.create_instances(
     BlockDeviceMappings=volumedevices,
     ImageId=ec2_config['server']['image_id'],
     UserData=user_data_string_b64,
     MinCount=1,
     MaxCount=1,
     InstanceType=ec2_config['server']['instance_type'],
     DryRun=False,
     KeyName='mykeypair123'
 )
