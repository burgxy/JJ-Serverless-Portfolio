# JJ-Serverless-Portfolio 
This git repo serves as a course work for an AWS/Serverless self tutorial, certification.  Using a simple HTML/JavaScript webpage as a usecase to build a personal online Portfolio    
  
  
  
    
At the end of the Course, I would have successfully deployed my sourcecode from a github or gitlab repository to an AWS S3 Bucket, that in turn would demonstrate my tangible understanding of the following technology under Amazon Web Services :-   


* AWS Lambda
* AWS S3
* AWS CloudFront
* AWS IAM
* AWS Route 53
* AWS SNS
* AWS CodeBuild
* AWS CodePipeline
  
  and these modern technologies:  
  
* ReactJS Framework/Library
* Git and Github
* Node Package Manager (NPM)
* Webpack module bundler
* Babel
* Jest
  
## Technology used (so far)  
  
* Atom Editor 
* Gedit Editor 
* Git and github  
* SSH  
* HTML  
* CSS  
* Font Awesome  
* Google Fonts  
  
## AWS Services (so far)  
  
* AWS S3 (Bucket)  
* AWS IAM  
* AWS Route53  
* AWS CloudFront  
* AWS CodeBuild 
* AWS Lambda
* AWS CodePipeline

## This is the breakdown of the inticipated flow of the Serverless Application 


 * Step 1  
A visitor visits your site (in this case halfknown.me.uk)  
  
 * Step 2  
they would go to your domain name which is managed by Route53  
  
  * Step 3  
route53 directs the site to cloudfront   
  
 * Step 4  
clouldfront hosts and redistributes your site ( Portfolio) accross to the world   
  
 * Step 5  
cloudfront gets the portfolio from S3  
  
 * Step 6  
the portfolio that gets to the user is made up of html , css, javasrcipt and some images ..  
  
 * Step 7  
html provides the structure of the portfolio   
  
 * Step 8  
css and images provides the look and feel

  
 * Step 9  
javascripts permit us to generate some of the html from the data and makes the portfolio interactive   

  
 * Step 10  
use a java library called react, designed by facebook .. 


 * Step 11  
and use another library called Babel that makes sure your portfolio works on all browsers . 

***************************************

the portfolio is developed on a local machine .. 

the sourcecode will be stored in github 

AWS codepipelines will coordinate other services to build and deploy to the S3 bucket mentioned .. 

AWS  codebuild gets it from github, runs task and build .. 






********************************

## Registered & Hosted Domain with Route53

halfknown.me.uk


## S3 Bucket (with Git repo files )

http://porfolio.halfknown.me.uk.s3-website-us-east-1.amazonaws.com/

# note
There's a typo when setting up my S3 Bucket , I spelt Portfolio wrong without the 't'

# Portfolio on S3 with Route53 (using the S3 Bucket or CloudFront as an A record)

porfolio.halfknown.me.uk

# Redirecting all HTTP trafic to HTTPS on CloudFront, and applied SSL Certificate from AWS  

https://d2di6b13dsc6yi.cloudfront.net/

# Getting all pushed Source to AWS CodeBuild. (with the Assistance of a Python Script)
