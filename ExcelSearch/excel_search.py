from copy import copy

import pandas as pd

df = pd.read_excel("excel_data.xlsx")
print("we are read the file.")

while True:
    # init_df = df
    pattern = input("название: ")
    list_of_words = pattern.split(" ")
    df_abc = df
    # df_abc = df_abc[df_abc["Полное наименование"].str.match(pattern)]
    for word in list_of_words:
        word = word.lower()
        df_abc = df_abc[df_abc["Полное наименование"].str.lower().str.contains(word)]
    print(df_abc.head(-1))



# for cell in df_abc.iteritems():
#     print(cell)