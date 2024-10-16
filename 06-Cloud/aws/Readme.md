# AWS Examples

## Pre-requisites

* Visual Studio extension AWS toolkit
* AWS shell [doc](https://github.com/awslabs/aws-shell) -> activate virtual environment for individual examples
* AWS CDK 
  ```bash
  sudo npm install -g aws-cdk
  ```
* for all examples you need AWS credentials stored in file credentials in folder $HOME/.aws

# Examples

## Query your AWS data
This example shows you, how to send queries to your AWS account. Example contains various listings of things like running ec2 instances or VPCs.

### How to run

  ```bash
  deactivate # turn off any other virtual environment
  cd query_aws_account
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python sample_queries.py
  ```