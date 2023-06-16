# ORM (object-Reletional MApping) -технология программирования, блогодаря которой разработчики могут использовать язык программ. для взаимодействия с реляционной базой данных (PostgreSQL, MySQL и тд) Вместо того чтобы писать сырые запросы(операторы SQL), вы будите писать код на языке программ. Это очень сильно ускооряет разработку приложения и бд, особенно на начальных этапах.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_db',
    user ='bakberdi',
    password ='1',
    host ='localhost', # 127.0.0.1 
    port =5432
)
