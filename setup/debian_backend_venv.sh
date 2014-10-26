#!/bin/bash

#git@github.com:diraol/trilhasp.git

#Run as setup/debian_virtualenv.sh from the folder up to this one

#checking if the current directory is the setup dir
#if it is, goes one level up.
curdir=${PWD##*/}
if [ "$curdir" == "setup" ]; then
  cd ..
fi

echo "Installing Virtual env prerequisites"
echo "sudo apt-get install  python-setuptools python-pip libmysqlclient-dev python-dev -y"
sudo apt-get install python-setuptools python-pip libmysqlclient-dev python-dev -y

echo "Install VirtualEnv"
echo "sudo pip install virtualenv"
sudo pip install virtualenv

echo "Creating a new virtualenv"
echo "virtualenv --no-site-packages venv"
virtualenv --no-site-packages venv

echo "Adicionando o virtualenv ao gitignore"
if [! grep -Fxq "venv" .gitignore ]; then
  echo "venv" >> .gitignore
fi

echo "Ativando o virtualenv"
echo "source ./venv/bin/activate"
source ./venv/bin/activate

echo "Instalando o Django"
pip install django

echo "Instalando o python-mysql e o ipython"
pip install mysql-python
pip install ipython

echo "Instalando dependências do projeto"
echo "Python social auth"
#pip install python-social-auth
