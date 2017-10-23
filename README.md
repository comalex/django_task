##Run project

> git clone https://github.com/comalex/django_task.git
> cd django_task

###Docker
> docker-compose build
> docker-compose up

### Manual

> python3 -m venv virtualenv_path 
> source virtualenv_path/bin/activate
> pip install -r requirements.txt
> python manage.py migrate
> python manage.py runserver

Open in browser `http://127.0.0.1:8000/`