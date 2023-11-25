import os
from pydantic import BaseSettings
from sqlalchemy import create_engine, Table, Column, Integer, String, LargeBinary, MetaData, insert, select
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import psycopg2

load_dotenv()
user_name = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("PORT")
db_name = os.environ.get("POSTGRES_PROD_DB_NAME")
load_dotenv(".env")


engine = create_engine(f"postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db_name}") 
metadata = MetaData()

music = Table('music', metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('name', String(255)),
  Column('author', String(255)),
  Column('music_file', LargeBinary),
  Column('genre', String(255))
) # создаём таблицу с полями id, name, author, music_file 

metadata.create_all(engine)

with open('hush.wav', 'rb') as f:
  music_file = f.read()

with engine.connect() as connection:
  result = connection.execute(insert(music), id=1, name='hush', author='author1', music_file=music_file)


with engine.connect() as connection:
  result = connection.execute(select(music).where(music.c.name == 'song1'))
  row = result.fetchone()

# Write the music file to a file
with open('retrieved_music_file.mp3', 'wb') as f:
  f.write(row['music_file'])