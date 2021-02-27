# InternetShop
Prerequisites
in terminal create new directory
with command 
  mkdir <directory name> 
  cd <directory name> 
 *instead of the name, enter the name of your directory 
 
 
Installation
1. Clone the repo
  git clone https://github.com/lolitagupta/InternetShop/
2. create a virtual environment 
  python -m venv env
  sourse env/bin/activate
3. Install apps
  pip3 install -r requirements.txt

DB
in shop/mypro/settings.py find 
  
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': '<db _name>',
      'USER': '<user_name>',
      'PASSWORD': '<pass>',
      'HOST': 'localhost',
      'PORT': 5432
  }
}
  
change <...> params on yours

Migrate models
  python3 manage.py makemigrations
  python3 manage.py migrate

Create superuser
  python3 manage.py createsuperuser
fill in the parameters with your data 

run the site on a local servite 
 python3 manage.py runserver

open and login on
  http://127.0.0.1:8000/admin/ 
add categories and products

open 
  http://127.0.0.1:8000/home/
and test
