import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sqlite3

# Connect to the database
conn = sqlite3.connect('airbnb_database.db')

# Create a cursor
cursor = conn.cursor()

# Query the database to get all the male user
cursor.execute("""SELECT COUNT(id) FROM train_user WHERE gender = 'MALE';""")
maleUser = cursor.fetchall()

# Query the database to get all the female user
cursor.execute("""SELECT COUNT(id) FROM train_user WHERE gender = "FEMALE";""")
femaleUser = cursor.fetchall()

# Print the results
print(f"{maleUser[0][0] / (maleUser[0][0] + femaleUser[0][0]) * 100:.2f}% of the users are male.")
print(f"{femaleUser[0][0] / (maleUser[0][0] + femaleUser[0][0]) * 100:.2f}% of the users are female.")

# concatenate the two lists
userGender = [maleUser[0][0], femaleUser[0][0]]
keys = ['male','female']

# define Seaborn color palette to use
palette_color = sns.color_palette('pastel')[0:2]
  
# plotting data on chart
plt.pie(userGender, labels=keys, colors=palette_color, autopct='%.0f%%')
plt.title("")
  
# displaying chart
#plt.show()

# save chart as image
#plt.savefig("UserGender.png")

cursor.close()
conn.close()