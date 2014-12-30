Provisioning notes for a new server, written in a raucous sitting room, everyone 
else playing Skulls and Roses.
+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-+-=-

## Required packages:

* nginx
* Python 3
* Git
* pip 
* virtualenv

eg, on Ubuntu:

  sudo apt-get install python3 python3-pip nginx git 
  sudo pip3 install virtualenv

## Nginx Virtual Host config:
* see nginx.template.conf
* replace SITE with fqdn

## Upstart Job:
* See gunicorn-upstart.template.conf
* Replace site

## Folder structure:
Assume a user at /home/username

/home/username
  -- sites
     -- SITE
        -- database
        -- source
        -- static
        -- virtualenv 
