# Week9_YZ

[![Python application test with Github Actions](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project3_SQL_YZ/actions/workflows/main.yml)

## Overview

This the repository for IDS 706 Data Engneering System individual project3. In this project, I generated a airbnb database and wrote sql queries using python libraries to create user profile of Airbnb including demographic information like age, gender, user language as well as service information like user destination for predicting which country a new user's first booking destination will be. I also built a command line interface to retrieve the plots of user information.  
Here is the flow chart and the demo video:

<img src=https://user-images.githubusercontent.com/110933007/200093798-d7498f34-962b-4a62-86f3-0c74bfc3b54e.png width=60% height=60%>

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

<img src=https://user-images.githubusercontent.com/110933007/199645134-d0603214-d3e8-4812-b6e9-bfd742d7baae.png width=40% height=40%>

### Step 2： Build database using sqlite3

```
python load_db.py
```

## Way to use


