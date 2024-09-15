# InsightGen

## Overview

InsightGen is a serverless application designed to provide comprehensive business insights from structured data. It uses AWS Lambda, DynamoDB, and a Vue.js frontend with Apollo Client.

## Project Structure

- `backend/` - Contains AWS SAM configuration and Lambda function code.
- `frontend/` - Contains Vue.js application with Apollo Client.

## Backend Setup

1. Install AWS SAM CLI and AWS CLI.
2. Package and deploy the backend using AWS SAM:
   ```bash
   cd backend
   sam package --template-file template.yaml --s3-bucket your-s3-bucket-name --output-template-file packaged.yaml
   sam deploy --template-file packaged.yaml --stack-name insightgen-stack --capabilities CAPABILITY_IAM

# InsightGen Project Description
InsightGen is an advanced serverless application designed to deliver actionable business insights from   raw data. Leveraging the power of AWS services and modern frontend technologies, InsightGen provides a   comprehensive solution for business intelligence and data visualization.

## Project Highlights:

### Backend Architecture:

AWS Lambda: Serverless compute service that handles data processing and interaction with DynamoDB. It   allows the application to scale automatically and handle varying loads efficiently.
Amazon DynamoDB: A fully managed NoSQL database that stores business insights and raw data. It is configured with a single table design for efficient data access and management.
API Gateway: Facilitates interaction between the frontend and backend services via RESTful APIs.
Frontend Architecture:

Vue.js: A progressive JavaScript framework used to build a dynamic and responsive Single-Page Application (SPA). It provides an intuitive interface for users to interact with and view business insights.
Apollo Client: Manages data fetching and state management from the GraphQL API, providing a seamless experience in retrieving and displaying data.
Key Features:

Dynamic Data Retrieval: The backend Lambda function processes requests to fetch and display insights stored in DynamoDB. It efficiently handles data retrieval and error management.
Interactive UI: The Vue.js frontend provides a user-friendly interface where users can view and interact with business insights. The Apollo Client facilitates smooth communication with the backend API.
Serverless Scalability: The use of AWS Lambda and DynamoDB ensures that the application can scale based on demand without requiring manual intervention.

# Technical Stack:

## Backend:

  ### AWS Lambda (Python 3.8)
  ### Amazon DynamoDB (NoSQL)
  ### AWS API Gateway (REST API)
  ### AWS SAM (Serverless Application Model) for deployment

## Frontend:

  ### Vue.js (JavaScript Framework)
  ### Apollo Client (GraphQL Client)
  ### Webpack and Babel for build tools


# Deployment:

## Backend Deployment:

Use AWS SAM to package and deploy the Lambda functions and DynamoDB table. Ensure that the Lambda function code is correctly uploaded to an S3 bucket and referenced in the AWS SAM template.
Frontend Deployment:

Develop the Vue.js application and configure Apollo Client to connect to the deployed API Gateway endpoint. Build the project and deploy the static assets to a hosting service such as AWS S3.
Getting Started:

#### Clone the Repository: 
  Clone the InsightGen repository to your local machine to access the project files and setup instructions.

## Backend Setup:
    Install AWS SAM CLI and AWS CLI.
    Package and deploy the backend using SAM commands.

## Frontend Setup:
    Install project dependencies and build the Vue.js application.
    Deploy the frontend to your preferred hosting service.
    Documentation and Support:

  README.md: Provides detailed setup instructions, project structure, and deployment notes.
  API Documentation: Includes endpoint specifications and usage guidelines.

## Conclusion:

InsightGen combines powerful serverless technologies with modern frontend frameworks to offer a robust solution for business data analysis. Its serverless architecture ensures scalability and cost-efficiency, while its interactive frontend provides a seamless user experience.
