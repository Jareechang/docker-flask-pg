DFP: Docker-Flask-Postgresql 
============================
**----- This is a work in progress -----**

A simple starter for running containerized Flask and postgresql docker instances

## Installation

1. Install [Docker Compose](https://www.docker.com/)
- Docker Engine will need to be installed as well

If you have **Vagrant** then use my [Vagrant-docker starter](https://github.com/Jareechang/vagrant-docker-starter):

```
git@github.com:Jareechang/vagrant-docker-starter.git && cd vagrant-docker-starter 
vagrant up
```

2. Clone started repository 
```
git clone git@github.com:Jareechang/docker-flask-pg.git
```

## Up and Running containers 

Defining Environment variables provided with **.env** file to define environments for running docker containers.

```
docker-compose build
docker-compose up -d
```

## Customizations 

TODO
