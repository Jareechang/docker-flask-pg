DFP: Docker-Flask-Postgresql 
============================
**----- This is a work in progress -----**

A simple starter for running containerized Flask and postgresql docker instances


## Installation

1. Install [Docker Compose](https://www.docker.com/)

- Docker Engine will need to be installed as well

2. Clone started repository 
```
git clone git@github.com:Jareechang/docker-flask-pg.git
```

## Up and Running containers 

1. Defining Environments variables
Provided with **.env** file to define environments for running docker containers

2. Building an image based on the **docker-compose.yml** 
```
docker-composer build
```

3. Run containers
```
docker-compose up -d
```

## Customizations 

TODO
