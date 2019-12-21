#!/usr/bin/env python
# coding: utf-8

# the title of the article   `<span class="headline">Maas verurteilt geplante US-Sanktionen</span>`
# 
# the comments               `article-comment`
# 
# the title of the user       `<class="article-comment-user>`
# 
# the article comment title   `<div class="article-comment-title"`

# In[27]:


import bs4 as bs
import urllib.request 
import requests
from lxml import html
from urllib.request import urlopen


sauce = urllib.request.urlopen('https://www.spiegel.de/politik/deutschland/nord-stream-2-heiko-maas-verurteilt-geplante-us-sanktionen-a-1300929.html')

soup = bs.BeautifulSoup(sauce, 'lxml')


# In[ ]:


for name in soup.find_all('span', {'class': 'headline'}):
    print(name.text)


# In[28]:


# print (soup.find_all('span'))


# In[95]:


for paragraph in soup.find_all('div', {"class": "article-comment"}):
#     name = paragraph.find_all('span', {'class': 'headline'})[0]
    author = paragraph.find_all('div', {'class': 'article-comment-user'})[0]
#     print(author.text.strip())
    article_comment_title =  paragraph.find_all('div', {'class': 'article-comment-title'})[0]
#     print(article_comment_title.text.strip())
    body_of_comment = paragraph.find_all('div', {'class': 'clearfix js-article-post-teaser'})[0]
    print(author.text.strip(), article_comment_title.text.strip(), body_of_comment.text.strip())
    print('='*100)


# In[ ]:


for paragraph in soup.find_all('div', {"class": "article-comment"}):
    author = paragraph.find_all('div', {'class': 'article-comment-user'})
#     print(author.text.strip())
    article_comment_title =  paragraph.find_all('div', {'class': 'article-comment-title'})
#     print(article_comment_title.text.strip())
    body_of_comment = paragraph.find_all('div', {'class': 'clearfix js-article-post-teaser'})
    print(author.text.strip(), article_comment_title.text.strip(), body_of_comment.text.strip())
    print('='*100)


# In[84]:


for author in soup.find_all('div', {'class': 'article-comment-user'}):
    print(author.text)
for title in soup.find_all('div', {'class':'article-comment-title'}):
    print(title.text)
#         for text in soup.find_all('div', {'class': 'clearfix js-article-post-teaser'}):
# #             print(author.text + title.text + text.text)
#                 print(author.text)


# In[83]:


for title in soup.find_all('div', {'class':'article-comment-user'}):
    print(title.text)


# In[79]:


body = soup.body
for div in soup.find_all('div', class_='article-comment'):
    print(div.text)


# In[19]:


for paragraph in body.find_all('p'):
    print (paragraph.text)  


# In[ ]:




