import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

dataset = pd.read_json("reviews.csv")
#dataset = pd.read_json("items2.json")
summarised_results = dataset["stars"].value_counts()
#plt.bar(summarised_results.keys(), summarised_results.values)
#plt.show()

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

words=" "
palabrasqueno = ['de', 'es', 'una', 'que', 'en', 'la', 'lo', 'se', '1a', 'el', 'por', 'pero', 
                 'para', 'muy','un','lo']
for msg in dataset["comment"]:
    for estano in palabrasqueno:
        msg = msg.replace( str(estano)+' ', '')
    msg = str(msg).lower()
    words = words+msg+" "
wordcloud = WordCloud(width=3000, height=2500,background_color='white').generate(words)
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 14
fig_size[1] = 7
#plt.show(wordcloud)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

