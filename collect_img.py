
# coding: utf-8

# In[4]:

#!/usr/bin/env python


import sys
import os
import re
import subprocess as spr


# クエリ検索したHTMLの取得
def get_HTML(query):

    html = spr.getstatusoutput("wget -O - https://www.bing.com/images/search?q=" + query)

    return html

# jpg画像のURLを抽出
def extract_URL(html):

    url = []
    sentences = html[1].split('\n')
    ptn = re.compile('<a href="(.+\.jpg)" class="thumb"')

    for sent in sentences:
        if sent.find('<div class="item">') >= 0:
            element = sent.split('<div class="item">')

            for j in range(len(element)):
                mtch = re.match(ptn,element[j])
                if  mtch >= 0:
                    url.append(mtch.group(1))

    return url

# ローカルに画像を保存
def get_IMG(dir,url):

    for u in url:
        try:
            os.system("wget -P " + dir + " " + u)
        except:
            continue


if __name__ == "__main__":

    argvs = sys.argv # argvs[1]: 画像検索のクエリ, argvs[2]: 保存先のディレクトリ(保存したい時のみ)
    query = argvs[1] # some images  e.g. leopard

    html = get_HTML(query)

    url = extract_URL(html)

    for u in url:
        print (u)

    # 画像をローカルに保存したいときに有効にする
    #get_IMG(argvs[2],url)


# In[3]:

import subprocess


# In[ ]:



