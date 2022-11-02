def userAge():

    # import libraries
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

    # Get the user age information from the database
    cursor.execute("""SELECT age, COUNT(id) FROM train_user WHERE age BETWEEN 0 AND 80 GROUP BY age ORDER BY age;""")
    userAge = cursor.fetchall()

    # create one list of age and one list of count
    age = []
    count = []
    for i in range(1, len(userAge)):
        age.append(userAge[i][0])
        count.append(userAge[i][1])

    result = "80% of airbnb users are between 25 and 35 years old."

    # plot a bar plot of the age and count
    plt.bar(age, count)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.xticks(np.arange(0, 80, 5))
    plt.title('User Age Distribution')
    #plt.show()

    # save chart as image
    plt.savefig("UserAge.png")

    cursor.close()
    conn.close()

    return result
