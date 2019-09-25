# RiskOfRain2 API

## What is Risk Of Rain 2

Risk Of Rain 2 is a video game first available in late March 2019. It is a third-person shooter roguelike game. You can control a character, buy items and play through different levels.

## Disclaimer

This project was made for a school assigment. The project is not hosted anymore on heroku.  
Furthermore the project was originally hosted on GitLab to use the CI/CD. You can check it at the following link : https://gitlab.com/MathieuSoSlow/RiskOfRain2API

## Introduction

RiskOfRain2 API aims to give access to a structured version of the data found on the website: https://riskofrain.fandom.com/wiki/Risk_of_Rain_2.
Here are the different type of data available:
- items
- achievements
- characters
- abilities
- enemies
- levels

The second part of the project lets the user create a hypothetical build from given items.

## The Wiki

### Data

You can navigate the wiki's API from the root at the following address: https://riskofrain2wiki.herokuapp.com
Data can be found under the following routes:
- `/items`
- `/achievements`
- `/characters`
- `/abilities`
- `/enemies`
- `/levels`


### Build

You can create a build with a post request on the route `/build` 
with the following format:
```
{
    "Soldier's Syringe": 3,
    "Lens-Maker's Glasses": 5
}
```
This will return a list of statistics, along with the achievements needed to unlock all the requested items.
```
{
    "stats": [
        "Increases attack speed by 45%.",
        "Your attacks have a 50% chance to 'Critically Strike', dealing double damage."
    ],
    "achievements": []
}
```

### Data Version

You can change the wiki's data with post requests on the route `/dataversions` with the following format:
- Update the current data
```
{
    "command": "update"
}
```
- Load data from a date
```
{
    "command": "load",
    "date": "20190605164827"
}
```
- Clear the data
```
{
    "command": "clear"
}
```


## Project Management

We used a DevOps approach while developing this project.

### Heroku

The service is hosted on Heroku. We have two environments:
- staging: https://staging-riskofrain2wiki.herokuapp.com
- production: https://riskofrain2wiki.herokuapp.com

### GitLab

#### Deployement

The project's source code is hosted on GitLab. A pipeline is set to run tests and check pep8 compliance for each commit.
The 'master' branch is used as a base to deploy on the staging environment, and a tagged commit is deployed on the production environment.

#### Pipeline

We use the GitLab pipeline to run our testsuite and check pep8 compliance. For deployment scenarios (master branch or tagged commit), actual deployement only happens if the pipeline passed. The result of the pipeline is displayed with a badge.

#### Code coverage

Pytest enables us to run our testsuite and output a code coverage percentage, which is displayed in a badge.

### Snyk

Snyk is used to check for vulnerabilities used packages, and merge requests are created when new vulnerabilities are introduced.

### Sentry

Sentry is used to get exception message for the deployed solution. We have two Sentry projects, on for production and one for staging.

### Notifications

We added a GitLab integration with slack in order to have notifications on commits, merges and issues.

### Issues and milestones

We use the Gitlab's issue board as well as milestones to manage objectives.

### Lockdown

The staging environment is locked behind a simple password system to avoid unwanted access.

## Documentation

An auto-generated documentation is available at `/swagger`.
