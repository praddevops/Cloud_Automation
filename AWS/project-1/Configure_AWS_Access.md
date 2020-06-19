AWS credentials have to be configure one of the ways described in https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html


# Using Shared Credentials to configure access to AWS

The shared credentials file has a default location of ~/.aws/credentials. You can change the location of the shared credentials file by setting the AWS_SHARED_CREDENTIALS_FILE environment variable.

This file is an INI formatted file with section names corresponding to profiles. With each section, the three configuration variables shown above can be specified: aws_access_key_id, aws_secret_access_key, aws_session_token. These are the only supported values in the shared credential file.

Below is a minimal example of the shared credentials file:

```
[default]
aws_access_key_id=<access key id here>
aws_secret_access_key=<secret access key here>
aws_session_token=baz
region_name=us-east-1
```

You may also have to configure other settings like default region, output type etc in ~/.aws/config depending on the type of resource you want to create