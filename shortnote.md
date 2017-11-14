visitor visits your site 

they would go to your domain name which is managed by Route53

route53 directs the site to cloudfront

clouldfront hosts and redistributes your site ( Portfolio) accross to the world 

cloudfront gets the portfolio from S3

the portfolio that gets to the user is made up of html , css, javasrcipt and some images .. 


html provides the strutture of the portfolio 

css and images provides the look and feel

javascripts permit us to generate some of the html from the data and makes the portfolio interactive 

use a java library called react, designed by facebook .. 

and use another another library called Babel that makes sure your portfolio works on all browsers . 

***************************************

the portfolio is developed on a local machine .. 

the sourcecode will be stored in github 

AWS codepipelines will coordinate other services to build and deploy to the S3 bucket mentioned .. 

AWS  codebuild gets it from github, runs task and build .. 

