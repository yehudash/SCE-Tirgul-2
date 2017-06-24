#!/bin/bash

sudo yum -y update && upgrade

sudo yum -y install git-all centos-relese-SCL python-setuptools python-setuptools-devel python-devel
sudo yum -y groupinstall "Development Tools"

sudo easy_install pip

git clonehttps://github.com/yehudash/SCE-Tirgul-2.git
cd SCE-Tirgul-2

#install our app requirements
sudo pip install -r requirements.txt

#create db
python db_create.py

#run app
nohup python run.py
