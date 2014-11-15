#!/bin/bash

#git@github.com:diraol/trilhasp.git

#Run as setup/debian_virtualenv.sh from the folder up to this one

#checking if the current directory is the setup dir
#if it is, goes one level up.
curdir=${PWD##*/}
if [ "$curdir" == "setup" ]; then
  cd ..
fi

if [ ! -d "venv" ]; then

  echo "Installing Virtual env prerequisites"
  echo "sudo aptitude install -y python-setuptools python-pip python-dev"
  sudo aptitude install -y python-setuptools python-pip python-dev

  echo "Installing system database dependencies"
  echo "sudo aptitude install postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis postgresql-server-dev-9.4 libpq-dev binutils libproj-dev gdal-bin python-gdal python-psycopg2"
  sudo aptitude install postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis-2.1 postgresql-9.4-postgis-2.1-scripts postgresql-server-dev-9.4 libpq-dev binutils libproj-dev gdal-bin python-gdal python-psycopg2

  #This commented code below is for installing geo dependencies from source. Not needed.
  #echo "Installing GEOS"
  #if [ ! -d "temp" ]; then
    #mkdir "temp"
  #fi
  #cd temp
  #wget http://download.osgeo.org/geos/geos-3.3.8.tar.bz2
  #tar xjf geos-3.3.8.tar.bz2
  #cd geos-3.3.8
  #./configure
  #make
  #sudo make install
  #cd ..

  #echo "Installing PROJ.4"
  #wget http://download.osgeo.org/proj/proj-4.8.0.tar.gz
  #wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz
  #tar xzf proj-4.8.0.tar.gz
  #cd proj-4.8.0/nad
  #tar xzf ../../proj-datumgrid-1.5.tar.gz
  #cd ..
  #./configure
  #make
  #sudo make install
  #cd ..

  #echo "Installing GDAL"
  #wget http://download.osgeo.org/gdal/gdal-1.9.2.tar.gz
  #tar xzf gdal-1.9.2.tar.gz
  #cd gdal-1.9.2
  #./configure
  #make
  #sudo make install
  #cd ..

  #cd ..
  #rm -rf temp

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
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate

#echo "Instalando dependências do projeto"
#echo "Python social auth"
#pip install python-social-auth
