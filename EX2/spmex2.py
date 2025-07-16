import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns

df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head(), df['label'].value_counts())

df['length'] = df['message'].apply(len)

sns.countplot(x='label', data=df)
plt.title("Spam vs Ham")
plt.show()

df[df['label']=='spam']['length'].plot.hist(bins=50, color='red', alpha=0.6, label='Spam')
df[df['label']=='ham']['length'].plot.hist(bins=50, color='blue', alpha=0.6, label='Ham')
plt.legend()
plt.title("Message Length")
plt.show()

spam_words = " ".join(df[df['label']=='spam']['message'])
ham_words = " ".join(df[df['label']=='ham']['message'])

WordCloud(stopwords=STOPWORDS, background_color='white').generate(spam_words).to_image().show()
WordCloud(stopwords=STOPWORDS, background_color='white').generate(ham_words).to_image().show()
