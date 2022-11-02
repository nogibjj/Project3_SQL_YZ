# Week9_YZ

[![Python application test with Github Actions](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml)

Generate a script that queries a database: MySQL, Sqlite, Spark or a cloud system. The query should be something useful to the user and be portfolio worthy.

## 1. Download dataset from kaggle

mkdir /home/codespace/.kaggle

cp /workspaces/Week9_YZ/kaggle.json /home/codespace/.kaggle

chmod 600 /home/codespace/kaggle/kaggle.json

cd /home/codespace/.kaggle

copy api from kaggle, download the dataset

cp train_users_2.csv.zip /workspaces/Week9_YZ



## 2. Create database

python load_db
