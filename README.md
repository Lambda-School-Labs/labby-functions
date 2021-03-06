# Labby

[![Maintainability](https://api.codeclimate.com/v1/badges/f9310d8480b61b88f0d4/maintainability)](https://codeclimate.com/github/Lambda-School-Labs/labby-functions/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f9310d8480b61b88f0d4/test_coverage)](https://codeclimate.com/github/Lambda-School-Labs/labby-functions/test_coverage)

## Overview

Labby is a growing collection of automation functions that support Lambda Labs operations.

## Architecture

Labby is a serverless application built on the [Serverless Framework](https://serverless.com) currently deployed to AWS. Labby uses various AWS services to allow for scale and reliability.

## Packages

The packages in Labby are broken up by the various services that Labby manages. Though, given that Labby enables integration between various services, the code in each package will probably reference other services.

See the README in each package for more details.

- Github: Manages provisioning and access to repositories based on active projects and team membership.
- Code Climate: Labs uses Code Climate to assess code quality, Labby helps integrate with Code Climate and gathers metrics.
- Slack: Allows Labby to interact with students and staff via Slack
- Mock Interviews: Labby helps with the Labs Mock Interview process
- Peer Reviews: Labby monitors peer review submissions (or lack thereof) to remind students and staff to submit their reviews.
- Labs Data: Much of Labby's activities are driven by data produced by operational activities in Labs.

## Configuration

Labby needs access to all sorts of APIs and data stores, which require secrets. These secrets are managed via AWS Secrets Manager.

Adding a secret:

```shell
aws secretsmanager create-secret --name <secret-name> --secret-string <secret-value>
```

Here are the secrets that need to be available for Labby:

### Github Credentials

Labby interacts with Github as a [Github App](https://developer.github.com/apps/):

| Secret Name                  | Secret Value                                        |
| ---------------------------- | --------------------------------------------------- |
| labby-github-api-app-id      | Client ID from the app settings                     |
| labby-github-api-key         | The downloaded app private key                      |
| labby-github-integration-id  | The integration ID created when installing the app  |
| labby-github-installation-id | The installation ID created when installing the app |

### Code Climate Credentials

Labby interacts with the Code Climate API using an [API key](https://developer.codeclimate.com/#overview):

| Secret Name                | Secret Value         |
| -------------------------- | -------------------- |
| labby-code-climate-api-key | Code Climate API key |

### Airtable Credentials

Labby interacts with Airtable using an [API key](https://airtable.com/api):

| Secret Name            | Secret Value     |
| ---------------------- | ---------------- |
| labby-airtable-api-key | Airtable API key |

## Labby Assets

The `assets` folder contains various static assets for use by the functions. Be aware that during deployment the `serverless-s3-deploy` plugin will automatically ship _everything in the assets folder_ to a _public, readable by the whole wide world web_ S3 bucket.

## Environment

You're going to need to create a `.env.yml` file in the root after you clone. It must contain:

- GITHUB_ORG_NAME: The name of the GitHub org for Labs student product and project repos
- GITHUB_APP_INTEGRATION_ID: The GitHub App Integration ID is the ID of your GitHub App. You can find it in the "About" section in the "General" tab of your GitHub App (Called App ID).
- GITHUB_APP_ORG_INSTALLATION_ID: For talking to the Github API
- GITHUB_APP_PRIVATE_KEY: The Github app private key
- CODE_CLIMATE_ACCESS_TOKEN: An API token for talking to Code Climate
- AIRTABLE_API_KEY: An API token for talking to AirTable
- SLACK_API_TOKEN: An API token for talking to Slack
- STUDENT_ACCOUNT_OU_ID: The ID of the student account OU (e.g. "ou-1234-12345678")
- ROOT_ACCOUNT_ID: The ID of the root account (e.g. 123456789123)

## Running Local

> If you are using aws profiles then you must have an env var AWS_PROFILE set to the profile name. (might as well add AWS_REGION to be safe)
>
> `export AWS_PROFILE=labby && export AWS_REGION=us-east-1`

- install [pipenv](https://github.com/pypa/pipenv)
- `pipenv install --dev`
- `pipenv shell`
- `python --version` # Python 3.7.3

TODO: Setup Serverless framework for python

- [Getting Started](https://serverless.com/framework/docs/getting-started/)
- `npx install serverless`
- [config]
- `sls invoke cloudside -f codeclimate_enqueue_all_product_repos`
