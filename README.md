# shake the rocks

[![Build Status](https://travis-ci.org/rozumalex/shaker.svg?branch=master)](https://travis-ci.org/github/rozumalex/shaker)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/shaker/blob/master/LICENSE)

---

Shake the rocks is online radio station with opportunity to upload tracks/

## Installation Guide


If you want to get a copy of this project for your personal usage,
please follow the instructions below.


### Clone the project to your local machine

```
git clone https://github.com/rozumalex/shaker
```


### Install and configure postgresql

```
sudo apt install postgresql libpq-dev build-essential python3-dev
sudo su postgres
psql
CREATE ROLE user WITH ENCRYPTED PASSWORD 'password';
CREATE DATABASE db_name;
GRANT ALL PRIVILEGES ON DATABASE db_name TO user;
ALTER ROLE user WITH LOGIN;
```
***Note:*** Then press Ctrl+D

### Install poetry

```
pip install poetry
```

### Install dependencies

***Note:*** you need to get to the directory with the project,
then you can run the command: 

```
poetry install
poetry shell
```

### Install and configure icecast2

```
sudo apt update
sudo apt upgrade
sudo apt install icecast2
```

### Install liquidsoap

```
sudo apt install liquidsoap
```

### Install certbot and get certificate

```
sudo apt install nginx
sudo apt install snapd
sudo snap install core
sudo snap install --classic certbot
sudo certbot --nginx -d example.com -d www.example.com
sudo systemctl restart nginx
```

### Configure Ubutnu Firewall
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

### Create .env file in project's folder and configure it:
```
DEBUG=on
SECRET_KEY="key"
DATABASE_URL=psql://test:test@127.0.0.1:5432/test
STATIC_URL=/static/
MEDIA_URL=/media/
```

### Install gunicorn
```
sudo apt install gunicorn
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rozumalex/shaker/blob/master/LICENSE) file for details.

