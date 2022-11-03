# Week9_YZ

[![Python application test with Github Actions](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml)

Generate a script that queries a database: MySQL, Sqlite, Spark or a cloud system. The query should be something useful to the user and be portfolio worthy.

## 1. Download dataset from kaggle

### Step 1: Installation

```
pip install kaggle
```
or put kaggle in the requirements.txt

### Step 2: Authentication

![image](https://user-images.githubusercontent.com/110933007/199645772-f2b33594-7520-4c4c-aab5-481671dbc00e.png)

User - Account - API

Create API token, download json file and then upload to GitHub Codespaces repo.

```
mkdir /home/codespace/.kaggle
cp /workspaces/Week9_YZ/kaggle.json /home/codespace/.kaggle
chmod 600 /home/codespace/kaggle/kaggle.json
cd /home/codespace/.kaggle
```

### Step 3: Download the dataset

copy api command and paste in the terminal

![image](https://user-images.githubusercontent.com/110933007/199645134-d0603214-d3e8-4812-b6e9-bfd742d7baae.png)

## 2. Build database

```
python load_db
```

## 3.Query


## 4. Command-line Interface


