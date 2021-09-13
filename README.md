# API <img align="center" alt="Marcos-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

Api do sistema de cardapio para restaurantes!

#Tecnologias utilizadas:
- Python 

- Django 

- Django Rest Framework

- Heroku



#Setup

- Criar diretório do projeto (mkdir nome_projeto)
- Criar venv (python -m venv venv)
- Add arquivos:

.gitignore

requirements.txt

- Install o Django
- Criar um projeto django (django-admin.py startproject setup .)
- Criar app das rotas (python manage.py startapp cardapio)
- Rodar o comando no terminal (python manage.py migrate) - criar as tabelas auth_user
- Cadastrar um super user (python manage.py createsuperuser)




#Documentação das Rotas (evidências)

#GetCardapio:

    [

    {
        "id": 1,
        "nome": "Fritas",
        "descricao": "Batata frita com cheddar e bacon"
    },
    
    {
        "id": 2,
        "nome": "Strogonoff",
        "descricao": "Arroz, e fritas"
    },

    ]
