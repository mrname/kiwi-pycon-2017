# kiwi-pycon-2017
Repository for Kiwi Pycon 2017 Talk (Docker Compose)

# Getting Started

## Install Docker and Docker Compose
To play along, you will need to start off by installing [docker](https://docs.docker.com/engine/installation/)
 and [docker-compose](https://docs.docker.com/compose/install/)  on your
workstation if they are not installed already.

## Clone this repository
```
git clone git@github.com:mrname/kiwi-pycon-2017.git && cd kiwi-pycon-2017
```

## Pull and Build Images
The example docker compose file needs to pull down many images. Since conference WIFI can be rough,
it is suggested that you pull these images prior to attending the talk. Furthermore, building the
primary application image requires downloading and installing python dependencies, so it is suggested
that you build the image prior to attending this talk.

### Pull Images
docker-compose pull

### Build Images
docker-compose build

