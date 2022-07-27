# Django Restful API Challenge

Implement a simple Restful API on Django using the following tech stack: Python, Django Rest Framework, AWS DynamoDB


## Getting Started
- [How to run this project?](#how-to-run-this-project)
- [Results and TestCases](#results-and-tests)
- [Deploy on AWS Lambda func by zappa](#deploy-on-aws-lambda)


# How to run this project

### 1. Clone repository:
```bash
>>> git clone https://github.com/M-Taghizadeh/Django-Restful-API-Challenge.git
>>> cd Django-Restful-API-Challenge
```

### 2. install requerments.txt
```bash
>>> python -m venv venv
>>> venv\Scripts\activate
# On Linux:
$ python -m venv venv
$ . venv/bin/activate

>>> cd .\config\
>>> pip install -r requirements.txt
```

### 3. AWS Cli Configuration
- Download AWS Cli from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and install it.

- on aws cli terminal:
```bash
>>> aws configure
```
- Enter your IAM informations:
```bash
$ AWS Access Key ID [None]: MYACCESSKEY
$ AWS Secret Access Key [None]: MYSECRETKEY
$ Default region name [None]: MYREGION
$ Default output format [None]: json
```

### 4. Aws DynamoDB

After entering the AWS Secret variables, we can use dynamodb migrator to create our nosql database.

```bash 
>>> python aws_dynamodb_migrator.py
```

After this, on AWS Dynamodb, we will see our database with the name "Device_DB", you can check it.
You can see it in the list of tables.
```bash
>>> aws dynamodb list-tables
```

### 5. Enter Your secret variables
- in settings.py : config/config/settings.py
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("YOUR_DJANGO_SECRET_KEY")
```

- in device_app/api/views.py
```python
# Get the dynamodb using boto3
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID",
    aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY",
    region_name = "YOUR_AWS_REGION_NAME",
)
```

### 6. Run server and use it :)
```bash
>>> python .\manage.py runserver
```


# Results and Tests
## Tests
This project is completely TestCase oriented and you can add other tests in the device_app/tests.py file. the six important and key test cases requested in the challenge have been successfully passed. You can test it with the following command.

```bash
>>> cd .\config
>>> python .\manage.py test   
```

- Tests Outpus
```bash
Found 6 test(s).
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 2.456s

OK
```

## Results
|HTTP Method |URL                                                                  |Functionality
|------------|---------------------------------------------------------------------|------------------
|POST        |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/   |Create new Device
|GET         |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/id1|Get Device by id
|GET         |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/all|Get all Devices

### Request 1 : Create New Device

|HTTP Method |URL                                                               |
|------------|------------------------------------------------------------------|
|POST        |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/|

```python
Body (application/json):
{
  "id": "/devices/id1",
  "deviceModel": "/devicemodels/id1",
  "name": "Sensor",
  "note": "Testing a sensor.",
  "serial": "A020000102"
}
```

### Response 1 - Success:
- **HTTP 201** Created

![test](docs/POST-200.png)

### Response 1 - Failure 1:
- **HTTP 400** Bad Request

If any of the payload fields are missing. Response body should have a descriptive error message for the client to be able to detect the problem.

![test](docs/POST-400.png)

### Response 1 - Failure 2:
- **HTTP 409** Conflict Error

If Item was already exists with this id.

![test](docs/POST-409.png)

<hr>

### Request 2 : Get Device 

|HTTP Method |URL                                                                  |
|------------|---------------------------------------------------------------------|
|GET         |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/id1|


### Response 2 - Success:
- **HTTP 200** OK

![test](docs/GET-200.png)

### Response 2 - Failure 1:
- **HTTP 404** Not Found

If the request id does not exist.

![test](docs/GET-404.png)


<hr>

### Request 3 : Get All Devices 

|HTTP Method |URL                                                                  |
|------------|---------------------------------------------------------------------|
|GET         |bjqutkwcyj.execute-api.us-east-1.amazonaws.com/dev/api/v1/devices/all|

### Response 3 - Success:
- **HTTP 200** OK

![test](docs/GET-ALL-200.png)

<hr>

# Deploy on AWS lambda

### Zappa - Serverless Python
Zappa makes it super easy to build and deploy server-less, event-driven Python applications (Django or Flask) on AWS Lambda + API Gateway + S3. 

- https://github.com/zappa/Zappa

We can deploy our python project on lambda and S3 buckets using zappa in the following three steps :)

```bash
$ pip install zappa
$ zappa init
$ zappa deploy
```

