# Exemplo básico de Geolocalização

Para este exercício, foi utilizado o banco de dados [PostgreSQL](https://www.postgresql.org) em conjunto com o [PostGIS](https://postgis.net)

### Instalação
Instale as bibliotecas necessárias rodando o comando:
```
$ pip install -r requirements.txt
```

Feito isso, criar o banco de dados com o comando:
```
$ createdb challenge
```

E para criar a estrutura no banco de dados:
```
$ cd src
$ ./manage.py migrate
```

### Executando
Para ver o projeto em funcionamento, basta rodar o comando dentro da pasta `src`:
```
$ ./manage.py runserver
```

Feito isso, basta acessar a URL [localhost:8000/api/traders/](http://localhost:8000/api/traders/)

### Testes
Para executar os testes, basta rodar o comando dentro da pasta `src`:
```
$ ./manage.py test
```
