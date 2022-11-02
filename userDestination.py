def userDestination():

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
    cursor.execute("""SELECT country_destination, COUNT(id) AS cd_num FROM train_user WHERE country_destination <> "NDF" GROUP BY country_destination ORDER BY cd_num DESC;""")
    userDestination = cursor.fetchall()

    # create one list of age and one list of count
    country = []
    destinationCount = []
    for i in range(len(userDestination)-1):
        country.append(userDestination[i][0])
        destinationCount.append(userDestination[i][1])

    result = "US is the destination of most airbnb users (75%), followed by France, Italy and United Kingdom."

    # plot a pie chart of the country and count
    palette_color = sns.color_palette('pastel')[0:5]
    plt.pie(destinationCount[0:5], labels=country[0:5], colors=palette_color, autopct='%.0f%%', pctdistance = 0.75, shadow=True,wedgeprops=wedgeprops, startangle=90)
    plt.title('User Destination Distribution')

    # save chart as image
    plt.savefig("UserDestination.png")

    cursor.close()
    conn.close()

    return result