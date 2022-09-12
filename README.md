<a name="readme-top"></a>

<h1 align="center">Dockerized FastAPI with Redis and Celery</h1>

![language](https://img.shields.io/badge/language-python-blue?style)


<!-- Project logo -->
<br />
<div align="center">
    <a href="https://github.com/Rochii/fastapi-celery-redis/">
    <!-- TODO: make the repository logo
      <img src="static/logo.png" alt="Logo" width="80" height="80">
    -->
  </a>

  <h3 align="center">Dockerized FastAPI with Redis and Celery</h3>

  <p align="center">
    Simple FastAPI implementation with NoSQL Redis and Celery workers using docker-compose and docker containers.
    <br />
    <a href="https://github.com/Rochii/fastapi-celery-redis/README.md"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>


<!-- Table of contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- About the project -->
## About The Project

<!--
[![Product Name Screen Shot][product-screenshot]](https://example.com)
-->

This project aims to learn and define a generalist structure to implement an efficient API using devops methodologies and new technologies.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built with


* [![Python][Python]][Python-url]
* [![Uvicorn][Uvicorn]][Uvicorn-url]
* [![Gunicorn][Gunicorn]][Gunicorn-url]
* [![Pydantic][Pydantic]][Pydantic-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![Redis][Redis]][Redis-url]
* [![Celery][Celery]][Celery-url]
* [![Docker][Docker]][Docker-url]
* [![Docker-compose][Docker-compose]][Docker-compose-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Getting started -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
* **Git**
* **Python3.10**
* **Virtualenv**
* **Docker**
* **Docker compose**
* **Make**

### Installation

1. Clone the repo and cd into:
   ```sh
   git clone https://github.com/Rochii/fastapi-celery-redis.git && cd fastapi-celery-redis
   ```
2. Create virtual environment for Python packages installation and source it:
   ```sh
   virtualenv venv && source venv/bin/activate
   ```
3. Install poetry:
   ```sh
   pip install poetry==1.1.15
   ```
4. Install poetry dependencies:
   ```sh
   poetry install
   ```
5. Create the **.env** file in project root directory as shown in **.env.example**:
   ```sh
   LOG_PATH=<localpath_to_store_logs>
   GUNICORN_WORKERS=<number_of_gunicorn_workers>
   CELERY_BROKER_URL=<redis_broker_url>
   CELERY_RESULT_BACKEND=<redis_backend_url>
   ```
6. Build docker images
   ```sh
   make build
   ```
7. Up docker images:
   ```sh
   make up
   ```

### More
To build, run and test and more... use magic of make.
```shell
make help
```
and you receive below list:
```text
Please use 'make <target>', where <target> is one of

  format             run all code formatters (isort, black)
  format-isort       run python import for library sorting
  format-black       run python code formatter according PEP8
  lint               run all linters (flake8, bandit, safety)
  lint-flake8        run linter to check coying style according PEP8
  lint-bandit        run linter to detect security issues in python code
  lint-safety        run linter to detect python dependency vulnerabilities
  test               run all tests (unitary, functional, integration)
  test-unitary       run unitary testing inside the container
  test-functional    run functional testing inside the container
  test-integration   run integration testing inside the container
  start              build, clean and up docker containers
  build              build docker container images
  clean              remove docker containers and networks
  up                 start docker containers in detached mode

Check the Makefile to know exactly what each target is doing.
Most actions are configured in 'pyproject.toml'.
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
1. Create new validation request:
    ```sh
    curl -X POST http://0.0.0.0:8888/v1/validation \
         -d '{ "text": "here some text to validate" }' \
         -H "Content-Type: application/json"
    ```
    and get response like below with `200 Success`
    ```json
    {
      "id":"ff78208b-883d-457b-9682-dc338635d934"
    }
    ```
2. Get validation results for that identifier:
    ```shell
    curl -X GET http://0.0.0.0:8888/v1/validation/ff78208b-883d-457b-9682-dc338635d934
   ```
   and get response like below with `200 OK`
   ```json
   {
        "id": "ff78208b-883d-457b-9682-dc338635d934",
        "text": "here some text to validate",
        "valid": 1
   }
   ```
3. For REST API Documentation please use: `http://0.0.0.0:8888/docs`

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- License -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Roger Truchero - truchero.roger@gmail.com

Project Link: [https://github.com/Rochii/fastapi-celery-redis](https://github.com/Rochii/fastapi-celery-redis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Acknowledgments -->
## Acknowledgments

* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [Readme Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links & images -->
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Python-url]: https://docs.python.org/3/
[Uvicorn]: https://img.shields.io/badge/uvicorn-000000?style=for-the-badge&logo=uvicorn
[Uvicorn-url]: https://www.uvicorn.org/
[Gunicorn]: https://img.shields.io/badge/gunicorn-000000?style=for-the-badge&logo=gunicorn
[Gunicorn-url]: https://gunicorn.org/
[Pydantic]: https://img.shields.io/badge/pydantic-000000?style=for-the-badge&logo=pydantic
[Pydantic-url]: https://pydantic-docs.helpmanual.io/
[FastAPI]: https://img.shields.io/badge/fastapi-000000?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Redis]: https://img.shields.io/badge/redis-000000?style=for-the-badge&logo=redis
[Redis-url]: https://redis.io/
[Celery]: https://img.shields.io/badge/celery-000000?style=for-the-badge&logo=celery
[Celery-url]: https://docs.celeryq.dev/en/stable/
[Docker]: https://img.shields.io/badge/docker-000000?style=for-the-badge&logo=docker
[Docker-url]: https://www.docker.com/
[Docker-compose]: https://img.shields.io/badge/docker_compose-000000?style=for-the-badge&logo=docker_compose
[Docker-compose-url]: https://docs.docker.com/compose/
