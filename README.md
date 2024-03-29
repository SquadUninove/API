# API <img align="center" alt="Marcos-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/SquadUninove/API/blob/main/LICENSE) 

## Api do sistema de cardapio para restaurantes!

## Sobre o Projeto

Back-end do sistema de cardápio para restaurantes, 
desenvolvido para a aula de Projetos do curso de ADS da Universidade Nove de Julho



## Tecnologias
- Python
- Django
- Django Rest Framework
- PostegreSQL
- Heroku




## Setup

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
- Install Rest Framework 
- Rodar o comando (python manage.py runserver)




# Documentação das Rotas

# Rotas-prato
## GET LIST_PRATOS
 https://api-squaduni.herokuapp.com/pratos

    [
    {
        "id": 1,
        "nome": "Baiao de dois",
        "preco": "25.90",
        "descricao": "fritas, salada e farofa"
    },
    {
        "id": 2,
        "nome": "Macarrao",
        "preco": "25.90",
        "descricao": "fritas e salada"
    }
    ]
    
## POST CREATE_PRATOS
 https://api-squaduni.herokuapp.com/pratos/create/
    
    {
          "nome": "Baiao de dois",
          "preco": "25.90",
          "descricao": "fritas e salada"
    }
    
 
   
## PUT UPDATE_PRATOS
 https://api-squaduni.herokuapp.com/pratos/update/1/ 

    {
        "id": 1,
        "nome": "Baiao de dois",
        "preco": "25.90",
        "descricao": "fritas, salada e farofa"
    }
   
## DELETE UPDATE_PRATOS
 https://api-squaduni.herokuapp.com/pratos/delete/1/   

  
## GET DETAIL_PRATOS
 https://api-squaduni.herokuapp.com/pratos/1/
 
 
## Para usar todas as rotas é necessário gerar o token, via rota de login!
![alt text](https://cdn.discordapp.com/attachments/879382939341844522/915000306503417856/unknown.png)
 
 ## Passar os parâmetros no headers, Key = Authorization | Value = Token (número do token) em cada teste de rota!
![alt text](https://cdn.discordapp.com/attachments/879382939341844522/914997792483721276/unknown.png)

