def userLanguage():

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

    # Get the user lanuage information from the database
    cursor.execute("""SELECT language, COUNT(language) AS lg_num FROM train_user GROUP BY language ORDER BY lg_num;""")
    userLanguage = cursor.fetchall()

    # create one list of language and one list of count
    language = []
    languageCount = []
    for i in range(1, len(userLanguage)):
        language.append(userLanguage[i][0])
        languageCount.append(userLanguage[i][1])

    # plot a bar chart of the language and count
    plt.bar(language, languageCount)
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.title('User Language Distribution')
    # save chart as image
    #plt.savefig("UserLanguage.png")

    # Number of users who speak English
    cursor.execute("""SELECT SUM(CASE WHEN language = "en" THEN 1 END) FROM train_user ;""")
    num_en = cursor.fetchall()[0][0]

    # Number of users who doesn't speak English
    cursor.execute("""SELECT SUM(CASE WHEN language <> "en" THEN 1 END) FROM train_user ;""")
    num_non_en = cursor.fetchall()[0][0]

    result1 = f"{num_en / (num_non_en + num_en) * 100:.2f}% of users speak English."
    result2 = f"Only {num_non_en / (num_non_en + num_en) * 100:.2f}% of users don't speak English."

    # Get non-English speaking user information from the database
    cursor.execute("""SELECT language, COUNT(language) AS lg_num FROM train_user WHERE language <> "en" GROUP BY language ORDER BY lg_num DESC;""")
    non_english_user = cursor.fetchall()

    # create one list of age and one list of count
    language2 = []
    languageCount2 = []
    for i in range(len(non_english_user)-1):
        language2.append(non_english_user[i][0])
        languageCount2.append(non_english_user[i][1])

    # plot a bar chart of the language and count
    fig,axes=plt.subplots(nrows=2, figsize=(12, 12))
    fig.tight_layout()
    
    axes[0].bar(language, languageCount)
    #axes[0].set_xlabel('Language')
    axes[0].set_ylabel('Count')    
    axes[0].set_title('User Language Distribution')
    #ax2 = fig.add_subplot(2,1,2)
    axes[1].bar(language2, languageCount2)
    axes[1].set_xlabel('Language')
    axes[1].set_ylabel('Count')
    axes[1].set_title('Non-Eglish User Language Distribution')
    # save chart as image
    fig.savefig("UserLanguage.png")

    cursor.close()
    conn.close()

    return result1, result2