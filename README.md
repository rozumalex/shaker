# shake the rocks

[![Build Status](https://travis-ci.org/rozumalex/shaker.svg?branch=master)](https://travis-ci.org/github/rozumalex/shaker)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/shaker/blob/master/LICENSE)

Shake The Rocks is online radio station with functionality of uploading tracks

---


## Installation Guide

This is an example how to deploy that project to production.  
1. [Prepare a Server](#prepare-a-server)  
  1.1 [Create a VPS](#create-a-vps)  
  1.2 [Configure Access Rights](#configure-access-rights)  
  1.3 [Configure Ubuntu Firewall](#configure-ubuntu-firewall)  
2. [Configure a Domain Name](#configure-a-domain-name)  
  2.1 [DNS Settings](#dns-settings)  
  2.2 [SSL Certificate](#ssl-certificate)  
3. [Install Icecast2](#install-icecast2)  
4. [Install Liquidsoap](#install-liquidsoap)  
5. [Install PostgreSQL](#install-postgresql)  
6. [Install Git](#install-git)  
7. [Install Poetry](#install-poetry)  
8. [Install Gunicorn](#install-gunicorn)  
9. [Configure the Application](configure-the-application)  
  9.1 [Env](#env)  
  9.2 [Nginx](#nginx)  
10. [Run the Application](#run-the-application)  

---

### Prepare a Server

---


#### Create a VPS

Add your ssh key while creating a server. If you don't have one, generate it:
```
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```

To see the public part of the key, use the following command from the home directory(if you used default key's file name and directory):
```
cat ~/.ssh/id_rsa.pub
```

---


#### Configure Access Rights

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

Connect to the server as root and remove it's ssh key:
```
ssh root@ip
rm ~/.ssh/authorized_keys
```

Reconnect to the server as user and edit sshd_config:
```
ssh user@ip
sudo nano /etc/ssh/sshd_config
```

Edit the following lines:
```
PubkeyAuthentication yes
PermitRootLogin no
```

Restart sshd.service:
```
sudo systemctl restart sshd.service
```

Disconnect from the server and edit ssh's config on your local machine for quick connection:
```
sudo nano ~/.ssh/config
```

Insert the following lines:
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

---


#### Configure Ubuntu Firewall

Connect to the server and configure ufw:
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


### Configure a Domain Name

---


#### DNS Settings

Manage DNS settings of your domain and add the following records:
```
Type      Host  Value TTL
A Record  @     ip    Automatic
A Record  www   ip    Automatic
```

---


#### SSL Certificate

Install certbot and create a certificate:
```
sudo apt install nginx snapd
sudo snap install core
sudo snap install --classic certbot
sudo certbot --nginx -d example.com -d www.example.com
sudo systemctl restart nginx
```

---


### Install Icecast2

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


### Install Liquidsoap

Install liquidsoap:
```
sudo apt install liquidsoap
```

---


### Install PostgreSQL

Install and configure PostgreSQL:
```
sudo apt install postgresql libpq-dev build-essential python3-dev psycopg2
sudo -u postgres psql
CREATE ROLE user WITH ENCRYPTED PASSWORD 'password';
ALTER ROLE user WITH LOGIN;
CREATE DATABASE db_name;
GRANT ALL PRIVILEGES ON DATABASE db_name TO user;
\q
```

---


### Install Git

Install git:
```
sudo apt install git
```

Clone the application:
```
git clone https://github.com/rozumalex/shaker
cd shaker
```

---


### Install Poetry 

Install poetry and create virtualenv:
```
sudo apt install python3-pip
pip3 install poetry
export PATH=$PATH:~/.local/bin
poetry install
poetry shell
```

---


### Install Gunicorn:

Install gunicorn:
```
sudo apt install gunicorn
```

---


### Configure the Application

---


#### Env

Create .env file:
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
ALLOWED_HOSTS=127.0.0.1, ip, example.com
```

---


#### Nginx

Configure nginx:
```
sudo nano /etc/nginx/sites-available/default
```

Edit default:
```
server {
	   listen 80 default_server;
	   listen [::]:80 default_server;
	   server_name ip;

        location /media/ {
                 root home/user/shaker/public;
                 expires 30d;
        }

        location /static/ {
                 root home/user/shaker/public;
                 expires 30d;
        }

	   location / {
		       proxy_pass http://127.0.0.1:8000;
	   }
}


server {
        location /media/ {
                root /home/user/shaker/public;
                expires 30d;
        }

        location /static/ {
                root /home/user/shaker/public;
                expires 30d;
        }

	   location / {
		      proxy_pass http://ip:8000;
	   }

        listen [::]:443 ssl ipv6only=on;
        listen 443 ssl;
        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf;
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

server {
        if ($host = www.example.com) {
            return 301 https://$host$request_uri;
        }

        if ($host = example.com) {
            return 301 https://$host$request_uri;
        }

        listen 80 ;
        listen [::]:80 ;
        server_name www.example.com example.com;
        return 404; #
}
```

Restart nginx:
```
sudo systemctl restart nginx
```

---


#### Application

Prepare application:
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

---


### Run the Application

Run:
```
gunicorn -w 3 --timeout 60 --max-requests 1 core.wsgi
```

---


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rozumalex/shaker/blob/master/LICENSE) file for details.

