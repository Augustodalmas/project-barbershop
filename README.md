# project-barbershop
Um projeto de barbearia - Em desenvolvimento

Para rodar o app: <br>
Primeiramente tenha o Python instalado.<br>
Após isso, crie uma Venv dentro do projeto<br>
```
Python -m venv venv
```
Após criar a Venv, Instale todos os requirements.txt
```
Pip install -r requirements.txt
```
Logo em seguida, de um migrate no banco de dados do Django:
```
Python manage.py migrate
```
Crie um superUser para mexer no admin: 
```
Python manage.py createsuperuser
```
E rode o servidor:
```
Python manage.py runserver
```

Para ver a listagem de barbearias acesse a url 
```
http://127.0.0.1:8000/list
```
E para adicionar itens no sistema, faça pelo admin, acessando:
```
http://127.0.0.1:8000/admin
```
