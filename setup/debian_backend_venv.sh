#!/bin/bash

#git@github.com:diraol/trilhasp.git

#Run as setup/debian_virtualenv.sh from the folder up to this one

#checking if the current directory is the setup dir
#if it is, goes one level up.
curdir=${PWD##*/}
if [ "$curdir" == "setup" ]; then
  cd ..
fi

#First check if the settings.py file from the project has already been created so the script can use it
if [ ! -f 'trilhasp/trilhasp/trilhasp/settings.py']; then
  echo "Please, first create the settings.py file on trilhasp/trilhasp/trilhasp/ directory so the script can use it"
  echo "Ending the script while the file is not created"
  exit 0
fi

if [ ! -d "venv" ]; then

  echo "Installing Virtual env prerequisites"
  echo "sudo aptitude install -y python-setuptools python-pip python-dev"
  sudo aptitude install -y python-setuptools python-pip python-dev

  echo "Installing system database dependencies"
  echo "sudo aptitude install postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis postgresql-server-dev-9.4 libpq-dev binutils libproj-dev gdal-bin python-gdal python-psycopg2"
  sudo aptitude install postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis-2.1 postgresql-9.4-postgis-2.1-scripts postgresql-server-dev-9.4 libpq-dev binutils libproj-dev gdal-bin python-gdal python-psycopg2

  echo "Installing nginx"
  sudo aptitude install nginx

  echo "Creating trilhasp db user"
  sudo -u postgres createuser trilhasp

  echo "Changing trilhasp db user password (enter your chosen passwrd)"
  sudo -u postgres psql --command '\password trilhasp'

  #https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/postgis/
  echo "Creating a spatial database with PostGIS 2.0 and PostgreSQL 9.1+"
  sudo -u postgres createdb --encoding=UTF8 --owner=trilhasp trilhasp

  echo "Creating postgis extensions"
  sudo -u postgres psql -d trilhasp -c "CREATE EXTENSION postgis;"
  sudo -u postgres psql -d trilhasp -c "CREATE EXTENSION postgis_topology;"

  echo "Install VirtualEnv"
  echo "sudo pip install virtualenv"
  sudo pip install virtualenv

  echo "Creating a new virtualenv"
  echo "virtualenv --no-site-packages venv"
  virtualenv --no-site-packages venv

fi

echo "Adicionando o virtualenv ao gitignore"
if [ ! $(grep -Fxq "venv" .gitignore) ]; then
  echo "venv" >> .gitignore
fi

echo "Ativando o virtualenv"
echo "source ./venv/bin/activate"
source ./venv/bin/activate

echo "Instalando dependências python"
pip install -r requirements.txt

echo "Seting up database"
cd trilhasp
echo "Current dir: $curdir"
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
