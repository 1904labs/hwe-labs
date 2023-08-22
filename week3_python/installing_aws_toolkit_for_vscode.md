# Hours with Experts - Week 3: How to install and use the AWS Toolkit extension for VsCode

## Installation

The AWS Toolkit Extension for VsCode is a useful set of tools that allow you to interact with AWS services (like S3) from within VsCode. It is not required to complete any part of this course, but you may find it helpful.

Download the toolkit from the visual studio marketplace with the below link, or search for it within VsCode itself by clicking the Manage icon in the bottom right, then clicking Extensions

https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode

## Create an AWS Connection

Once the extension is installed, you can use the shortcut ctrl + shift + p (Windows) or shift + cmd + p (Mac) to open the command palette. 

From there, select AWS: Connect to AWS -> Add New Connection

Select AWS Explorer and in the bottom right, select the 'Or add IAM User Credentials' option. Select 'Edit file directly', Add your access key and secret key under [default] in the credentials file.

## Use the AWS Toolkit

Once this has been configured, you should be able to connect to the AWS environment. You can repeat the shortcut mentioned above to get to the command palette and select the default profiled you just configured. 

You should see an AWS tab on the left side of VsCode. 

Select the service you wish to use.For example, if you select S3, you should be able to see any data you write to S3 as part of this course.