# shake the rocks

[![Build Status](https://travis-ci.org/rozumalex/shaker.svg?branch=master)](https://travis-ci.org/github/rozumalex/shaker)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/shaker/blob/master/LICENSE)

---

Shake The Rocks is online radio station with functionality of uploading tracks

## Installation Guide

This is an example how to deploy that project to production.
1. [Server Preparation](#server-preparation)
2. [Domain Name Configuration](#domain-name-configuration)
3. [Icecast2 Installation](#isecast2)
4. [Liquidsoap Installation](#liquidsoap)
5. [Application Installation](#application-installation)

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
sudo ufw allow 8080/tcp
sudo ufw allow 8443/tcp
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
```

---

### Icecast2

Install icecast2:

```
sudo apt install icecast2

sudo su
cd /etc/letsencrypt/live/example.com
cat fullchain.pem privkey.pem > /usr/share/icecast2/fullchain.pem
chmod 666 /usr/share/icecast2/fullchain.pem
sudo user

sudo nano /etc/icecast2/icecast.xml
```

Configure icecast.xml:
```
<icecast>
    <location>City</location>
    <admin>email@example.com</admin>\
    
    <limits>
        <clients>100</clients>
        <sources>2</sources>
        <queue-size>524288</queue-size>
        <client-timeout>30</client-timeout>
        <header-timeout>15</header-timeout>
        <source-timeout>10</source-timeout>
        <burst-on-connect>1</burst-on-connect>
        <burst-size>65535</burst-size>
    </limits>

    <authentication>
        <source-password>new-source-password</source-password>
        <relay-password>new-relay-password</relay-password>
        <admin-user>new-admin-name</admin-user>
        <admin-password>new-admin-password</admin-password>
    </authentication>
    
    <hostname>ip</hostname>

    <listen-socket>
        <port>8080</port>
    </listen-socket>

    <listen-socket>
        <port>8443</port>
        <ssl>1</ssl>
    </listen-socket>

    <http-headers>
        <header name="Access-Control-Allow-Origin" value="*" />
    </http-headers>

    <mount>
        <mount-name>/stream</mount-name>
        <charset>UTF-8</charset>
    </mount>

    <fileserve>1</fileserve>

    <paths>
        <basedir>/usr/share/ice2</basedir>
        <logdir>/var/log/icecast2</logdir>
        <webroot>/usr/share/icecast2/web</webroot>
        <adminroot>/usr/share/icecast2/admin</adminroot>

        <alias source="/" destination="/status.xsl"/>

        <ssl-certificate>/usr/share/icecast2/fullchain.pem</ssl-certificate>
        
    </paths>

    <logging>
        <accesslog>access.log</accesslog>
        <errorlog>error.log</errorlog>
        <loglevel>3</loglevel>
        <logsize>10000</logsize>
    </logging>

    <security>
        <chroot>0</chroot>
    </security>
</icecast>
```

Restart icecast2:
```
sudo systemctl restart icecast2
```

---

### Liquidsoap

Install liquidsoap:
```
sudo apt install liquidsoap
```

### Application Installation

Install and configure PostgreSQL
```
sudo apt install postgresql libpq-dev build-essential python3-dev psycopg2
sudo su postgres
psql
CREATE ROLE user WITH ENCRYPTED PASSWORD 'password';
ALTER ROLE user WITH LOGIN;
CREATE DATABASE db_name;
GRANT ALL PRIVILEGES ON DATABASE db_name TO user;
\q
su user
```

Install git:
```
sudo apt install git
```

Clone application:
```
git clone https://github.com/rozumalex/shaker
cd shaker
```

Install poetry and create virtualenv
```
sudo apt install python3-pip
pip3 install poetry
export PATH=$PATH:~/.local/bin
poetry install
poetry shell
```

#### Create .env file:
```
cd shaker
nano .env
```

Configure .env:
```
DEBUG=on
SECRET_KEY="key"
DATABASE_URL=psql://user:password@127.0.0.1:5432/db_name
STATIC_URL=/static/
MEDIA_URL=/media/
```

Install gunicorn:
```
sudo apt install gunicorn
```

Run the server:
```
gunicorn -w 5 --timeout 60 --max-requests 1 core.wsgi
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rozumalex/shaker/blob/master/LICENSE) file for details.

