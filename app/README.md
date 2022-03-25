# {{SERVICE_NAME}}

## Configuration

### Prerequisites
* Python 3.8
* NPM

### Set up
Install `serverless` and `serverless-offline` executing:
```shell
$ npm i serverless --save-dev
$ npm i serverless-offline --save-dev
```

### Executing locally
To execute your API locally, execute the following command:
```shell
$ serverless ofline start --stage local
```

### Deploying

To deploy your API, execute the following command:
```shell
serverless deploy --stage <env> --aws-profile <PROFILE>
```

Your AWS profile must have permissions to deploy. The `<env>` should be a valid one based on `vars.yml`.