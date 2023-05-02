import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import sys

sys.stdout.reconfigure(encoding='utf-8')

plt.rcParams['font.family'] = ['sans-serif', 'otf']

num_pages = 5

keywords = []

for page in range(1, num_pages + 1):

    url = f"https://search.naver.com/search.naver?query=지진&where=news&start={page*10+1}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title_selector = ".news_tit"

    titles = soup.select(title_selector)

    excluded_keywords = ["지진", "문자"]

    for title in titles:
        keyword = title.get_text().strip()
        if all(keyword not in excl_keyword for excl_keyword in excluded_keywords):
            keywords.append(keyword)

plt.figure(figsize=(10, 10))
ax = sns.scatterplot(x=range(1, len(keywords) + 1), y=keywords, size=5, sizes=(200, 1000), hue=range(1, len(keywords) + 1), palette="viridis", legend=False)
plt.xlabel("Index")
plt.ylabel("Keyword")
plt.title("Keywords from Naver Search")
plt.xticks(range(1, len(keywords) + 1))

ax.set_yticklabels(labels=keywords, fontdict={'fontfamily': 'sans-serif'})

plt.show()
