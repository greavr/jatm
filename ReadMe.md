# Just Another Task Manager

Simple task manager using two layer basic micro-service architecture.

## Getting Started

07/03/2019 - Application currently runs all in the front end. This is a Python / Flask based application, which will run in docker. To get started type the following commands:
```
git clone https://github.com/greavr/jatm.git
cd jatm\Python\code
pip install -r requirements.txt
export FLASK_APP=index.py
flask run
```
This will run a web version of the site accessible via http://localhost:5000
Any code changes will require a Flask restart:

```
CTRL+C in the console
flask run
```


### Prerequisites

What you need to install:

```
Python 3.6
pip
docker
GCP Tooling
```

### Installing

Install Docker:
[Docker CE](https://docs.docker.com/install/)

Install Python:
[Python 3.6](https://www.python.org/downloads/)

Install Pip (After installing Python):
[Pip](https://pip.pypa.io/en/stable/installing/)

Install Google Cloud SDK
[GCP SDK](https://cloud.google.com/sdk/)

## Deployment

If you want to see the packaged app running as a docker file, there is a working Docker file one step below the code folder, found \jatm\Python
To run this docker container complete the following command:
```
docker build -t front-end . && docker run --name fronty -d -p 5000:5000 front-end
```
You can kill the container with the command:
```
docker kill fronty
```



## Built With


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Rick Greaves** - *Initial work* - [PurpleBooth](https://github.com/greavr)
* **Monica**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Lots of soda!
