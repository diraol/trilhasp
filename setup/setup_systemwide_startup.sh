#!/bin/bash
#referebce: http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

#Just to have a good tree reference
curdir=${PWD##*/}
if [ "$curdir" == "setup" ]; then
  cd ..
fi


echo "Installing nginx"
sudo aptitude install nginx


echo "adding trilhasp user to nginx group (www-data) and www-data user to trilhasp group,"
echo "       to avoid for permissions problems"
sudo adduser trilhasp www-data
sudo adduser www-data trilhasp


echo "sym-linking nginx setup file to the system"
sudo ln -s /home/trilhasp/trilhasp/trilhasp_nginx.conf /etc/nginx/sites-enabled/


echo "Deploying static files"
# activating venv
source venv/bin/activate
#changing directory
cd trilhasp
#collecting file
python manage.py collectstatic
#returning from directory
cd ..


echo "Installing uwsgi system-wide"
sudo pip install uwsgi

echo "Creating directory to run uwsgi on emperor mode"
sudo mkdir -p /etc/uwsgi/vassals
sudo chown -R www-data:www-data  /etc/uwsgi

echo "Linking trilhas_uwsgi file to the config directory"
sudo ln -s /home/trilhasp/trilhasp/trilhasp_uwsgi.ini /etc/uwsgi/vassals/


echo "Making uwsgi startup with system boot"
echo "Altering rc.local"
sed 's@exit\s0@/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data\n&@' rc.local > tempfile_rclocal
sudo cp tempfile_rclocal /etc/rc.local
rm tempfile_rclocal

echo "Configuration ended"
