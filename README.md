# shake the rocks

[![Build Status](https://travis-ci.org/rozumalex/shaker.svg?branch=master)](https://travis-ci.org/github/rozumalex/shaker)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/shaker/blob/master/LICENSE)

---

Shake the rocks is online radio station with opportunity to upload tracks

## Installation Guide

This is an example how to deploy that project to production.
1. [Server Preparation](#server-preparation)
2. [Domain Name Configuration](#domain-name-configuration

---

### Server Preparation

#### Create a VPS

Add your ssh key while creating a server. If you don't have one, generate it:
```
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```

To see the public part of the key, use the following command from the home directory(if you used default key's file name):
```
cat .ssh/id_rsa.pub
```

#### Create a new user and configure connection via ssh

Connect to the server and create a new user:
```
ssh root@ip
adduser user
adduser user sudo
su alex
```

Disconnect form the server and add the ssh key to the created user:
```
ssh-copy-id -i ~/.ssh/id_rsa user@ip
```

Connect to the server as root and remove the ssh key:
```
ssh root@ip
cd ~/.ssh
rm authorized_keys
```

Reconnect to the server as user and edit sshd_config:
```
ssh user@ip
sudo nano /etc/ssh/sshd_config
```

Edit the next lines:
```
PubkeyAuthentication yes
PermitRootLogin no
```

Restart sshd.service:
```
sudo systemctl restart sshd.service
```

Disconnect from the server and edit ssh's config for quick connection on your local machine:
```
sudo nano ~/.ssh/config
```

Insert the next lines:
```
Host servername
     HostName ip
     User user
```

Connect to the server and upgrade:
```
ssh servername
sudo apt update
sudo apt upgrade
sudo reboot
```

#### Configure Ubuntu Firewall

Connect to the server and configure:
```
ssh servername
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

---

### Domain Name Configuration

#### Get a domain name

Manage DNS settings of your domain and create following records:
```
Type      Host  Value TTL
A Record  @     ip    Automatic
A Record  www   ip    Automatic
```

#### Get SSL Certificate

Install certbot and get certificate:
```
sudo apt install nginx
sudo apt install snapd
sudo snap install core
sudo snap install --classic certbot
sudo certbot --nginx -d example.com -d www.example.com
sudo systemctl restart nginx



#### Clone the project to your local machine

```
git clone https://github.com/rozumalex/shaker
```


#### Install and configure postgresql

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

#### Install poetry

```
pip install poetry
```

#### Install dependencies

***Note:*** you need to get to the directory with the project,
then you can run the command: 

```
poetry install
poetry shell
```

#### Install and configure icecast2

```
sudo apt update
sudo apt upgrade
sudo apt install icecast2
```

#### Install liquidsoap

```
sudo apt install liquidsoap
```
```


#### Create .env file in project's folder and configure it:
```
DEBUG=on
SECRET_KEY="key"
DATABASE_URL=psql://test:test@127.0.0.1:5432/test
STATIC_URL=/static/
MEDIA_URL=/media/
```

#### Install gunicorn
```
sudo apt install gunicorn
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rozumalex/shaker/blob/master/LICENSE) file for details.

