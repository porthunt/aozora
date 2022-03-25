# aozora

Aozora allows you to create an API skeleton using API Gateway + Lambda functions using Serverless Framework.

It create a HTTP API on API Gateway + lambda functions for each endpoint.

## Overview

```shell
./aozora.py --name my-api
cd my-api
npm i serverless --save-dev
npm i serverless-offline --save-dev
sls offline start --stage local
```

You can set up another location to create the directory using:
```shell
./aozora.py --name my-api --location ~/Coding
```

API folder structure:

```
my-api
├── README.md
├── .gitignore
├── .npmignore
├── Makefile
├── requirements.txt
├── requirements-dev.txt
├── serverless.yml
├── vars.yml
├── tests
|   └── ...
└── app
    ├── errors.py
    ├── settings.py
    ├── models
    |   └── response.py
    └── endpoints
        ├── __init__.py
        └── others.py
```

> _Some `__init__.py` were not included for easier readability._

## Configuring API

After creating your API, you can modify stuff on `serverless.yml`. It's possible to modify the function timeouts, memory, permissions for the role, etc.

For references, please refer to the [official serverless framework guide](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml).