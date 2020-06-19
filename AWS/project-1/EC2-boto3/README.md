ec2.yaml contains the ec2 configuration that will be plugged to boto3 script `create_ec2.py` to create EC2 instance in AWS platform. 

ec2.yaml contains instance type, ami id, volumes and their mount path and filesystem type, ssh public key to use to login to ec2.

To run this script: `python3 create_ec2.py`

Note: The linux system on which the boto3 script is executed should have credentials preconfigured