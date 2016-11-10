Test-Luizalabs
==========================

Requisitos
----------

Python 3
Virtualenv


Configuração
------------

Criar virtualenv: ::

    virtualenvwapper ou pyenv virtualenv


Install requirements via ``pip``: ::

    pip install requirements.txt


Criar tabelas do banco de dados: ::
    ./manage.py migrate


Rodar o projeto: ::
    ./manage.py runserver 


Criar um superuser: ::
	./manage.py createsuperuser