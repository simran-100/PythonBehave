# Behave POC
This is a POC done for understanding the use of [behave](https://behave.readthedocs.io/en/stable/index.html)

## Setup
To run this project you need to have python 3.x (Validated with with 3.8)

It is recommended to use pipenv. 

### Install depenndencies 
Using Pip Env
```
pipenv install
```

using pip
```
pip install -r requirements.txt
```

### Install allure reports (optional)
Install as specifed in [docs](https://github.com/allure-framework/allure2) 

Note: This is only needed if you need to see allure reports locally.

## Running the tests

Run all the tests is simplist approach.
```
behave
```
By default the [dev.json](./dev.json) will be used as the config.

To run the tests with different config file
```
behave --define env=qa  
```
These is controlled by the code in [environment.py](./features/environment.py)

To run the tests that are tagged as wip
```
behave --tags=wip  
```

To run tests with results to allure reports and view them.
```
behave --format=allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

## Code overview

.

|____.gitignore => files ignored in pushing to Server

|____.flake8  => python coding standards

|____requirements.txt => python dependency installed via pip

|____Pipfile => python dependency installed via pipenv

|____Pipfile.lock => python dependency used by pipenv for versions you are not supposed to change this

|____dev.json =>  Sample Config json

|____qa.json =>  Sample Config json

|____behave.ini => Controling beave outputs 

|____features

| |____e2e.feature => Sample feaute with Data driven

| |____e2e2.feature => Sample feaute with tag

| |____steps

| | |____e2e.py => All the steps. 

| |____environment.py => File which loads the configs based on env

|____README.md => This file

|____.github

| |____workflows

| | |____allure-python-behave.yml => Git hub action.

|____data => All the data which we use in tests

| |____ETOE2.json

| |____ETOE1.json

## Continous testing using Github actions
The system is configured to run the tests every time code is pushed. The test results are published github pages. You can view the results [here](https://pyxisperformance.github.io/behavePOC/)

## TODO items

- [ ] Run the tests at timely interval.
- [ ] Setup git brnaching rules.


