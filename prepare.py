import pandas as pd
import re
import os
import sqlite3
import MeCab
from tqdm import tqdm
from share import begin, end

initialises = True
if __name__ == '__main__':
    # tweet to corpus
    df = pd.read_csv('./data/tweets.csv')

    df = df[df['source'].str.match(r'.*(Twitter Web Client|Twitter for Android|TweetDeck).*')]
    df = df[~df['text'].str.startswith('RT @')]

    tweets = df['text']

    reply_to = r'@[\w]+'
    url = r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
    for deleted in [reply_to, url]:
        tweets = tweets.map(lambda s: re.sub(deleted, ' ', s))

    pd.DataFrame({'text': pd.Series(tweets)}).to_csv('corpus.csv')

    # corpus to database
    tagger = MeCab.Tagger("-O chasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
    tagger.parse('')

    path_db = 'frequency.db'
    if initialises:
        if os.path.exists(path_db):
            os.remove(path_db)
    conn = sqlite3.connect(path_db)
    curs = conn.cursor()

    if initialises:
        curs.execute('create table stocks(word0, word1, word2)')

    for tweet in tqdm(tweets):
        words = []
        node = tagger.parseToNode(tweet)
        while node:
            word = node.surface
            if word not in "　「」『』（）〈〉《》、。，．！？":
                words.append(word)
            node = node.next
        words = [begin] + words + [end]
        for i in range(len(words) - 2):
            curs.execute("insert into stocks values(?, ?, ?)", (words[i], words[i+1], words[i+2]))

    conn.commit()
    conn.close()