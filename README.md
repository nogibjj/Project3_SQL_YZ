# Project3_SQL_YZ

[![Python application test with Github Actions](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml)

## Overview

This the repository for IDS 706 Data Engneering System individual project3. In this project, I generated an airbnb database and wrote sql queries using python libraries to create user profile of Airbnb including demographic information like age, gender, user language as well as service information like user destination for predicting which country a new user's first booking destination will be. I also built a command line interface to retrieve the plots of user information.  
Here is the flow chart and the demo video:

<img src=https://user-images.githubusercontent.com/110933007/200093798-d7498f34-962b-4a62-86f3-0c74bfc3b54e.png width=80% height=80%>

## Dataset

The dataset comes from Kaggle: [Airbnb New User Bookings](https://www.kaggle.com/competitions/airbnb-recruiting-new-user-bookings). It contains demographics, web session records, and some summary statistics of airbnb users. By building user profile and accurately predicting where a new user will book their first travel experience, Airbnb can share more personalized content with their community, decrease the average time to first booking, and better forecast demand.

## Methodology

### Step 1: Using kaggle API to read dataset to csv.

#### Installation
```
pip install kaggle        # or put kaggle in the requirements.txt
```

#### Authentication

User - Account - API - create new API token - upload the json file to GitHub repo.
In Codespaces, excute the following code to move the api token to the home directory.
```
mkdir /home/codespace/.kaggle
cp /workspaces/Week9_YZ/kaggle.json /home/codespace/.kaggle
chmod 600 /home/codespace/kaggle/kaggle.json
cd /home/codespace/.kaggle
```

#### Download the dataset
copy api command and paste in the terminal:

<img src=https://user-images.githubusercontent.com/110933007/199645134-d0603214-d3e8-4812-b6e9-bfd742d7baae.png width=60% height=60%>

### Step 2： Create a database using sqlite3

In load_db.py, I wrote three functions to create a database connection to a SQLite databse, create a table in the database, and load data from csv file to the database. The created database is called *airbnb_database.db*
Excute the code to create the database:
```
python load_db.py
```

### Step 3: Query user information from the database to build user profile

Here are the SQL queries that I used to extract user information from the database:

```
SELECT age, COUNT(id) FROM train_user WHERE age BETWEEN 0 AND 80 GROUP BY age ORDER BY age;
SELECT country_destination, COUNT(id) AS cd_num FROM train_user WHERE country_destination <> "NDF" GROUP BY country_destination ORDER BY cd_num DESC;
SELECT COUNT(id) FROM train_user WHERE gender = 'MALE';
SELECT COUNT(id) FROM train_user WHERE gender = "FEMALE";
SELECT language, COUNT(language) AS lg_num FROM train_user GROUP BY language ORDER BY lg_num;
SELECT SUM(CASE WHEN language = "en" THEN 1 END) FROM train_user ;
SELECT SUM(CASE WHEN language <> "en" THEN 1 END) FROM train_user ;
SELECT language, COUNT(language) AS lg_num FROM train_user WHERE language <> "en" GROUP BY language ORDER BY lg_num DESC;
```

### Step 4：Build a command line interface to retrieve user profile

I used the typer library in python to build a command-line interface to retrieve the user information of airbnb and save the plots. 

<img src=https://user-images.githubusercontent.com/110933007/200096237-7c865ca6-6a5b-4968-96a6-dda5743b9d46.png width=80% height=80%>

<img src=https://user-images.githubusercontent.com/110933007/200096299-53936220-2286-4f29-8ffd-644f074f1e22.png width=80% height=80%>



## Way to use

```
python cli-tool.py --help
python cli-tool.py -- getuserage
python cli-tool.py -- getuserdestination
python cli-tool.py -- getusergender
python cli-tool.py -- getuserlanguage
```
