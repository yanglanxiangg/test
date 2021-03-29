from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords  
import math
import time

# Only frequency of the terms in the document is calculated for ranking currently

token_freq = {}
token_post = {}
doc_id = {}

# Temporary seek function
def sek(query):
    with open("merged.txt",'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(query):
                return line

# Load doc_id
with open("mergedDocid.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                break
            line = line.split('----')
            doc_id[int(line[0])] = line[1].replace('\n','')

numDoc = len(doc_id.keys())

def wordPos(file1):
    word_pos = {}
    length = 0
    with open(file1,"r",encoding = 'utf-8') as file:
        lines = file.readlines()
        length = 0
        for line in lines:
            token = line.split('----')[0]
            word_pos[token] = length
            if len(line) == 1:
                print(line)
            else:
                length += len(line) + 1
    return word_pos

def tfidf(query,wp,file):
    post_score = {}
    for q in query:
        # If the query is in the corpus
        if q in wp.keys():
            pos = wp[q]
            file.seek(pos)
            line = file.readline()
            line = line.split("----")
            freq = int(line[1])
            post = eval(line[2])
            post_length = len(post.keys())

            for key,value in post.items():
                key = int(key)
                tf = 1 + math.log10(value[0])
                idf  = math.log10(numDoc/(post_length + 1))
                score = tf * idf
                if key not in post_score:
                    post_score[key] = score + value[1]
                else:
                    post_score[key] += score + value[1]
    
    d = {k: v for k, v in sorted(post_score.items(), key=lambda item: item[1], reverse = True)}
    if len(d.keys()) > 10:
        d = {k: d[k] for k in list(d)[:10]}
        return d
    else:
        return d


def stopWord(query, stopwords):
    count = 0
    for q in query:
        if q.lower() in stopwords:
            count += 1
    if count/len(query) < 0.3:
        query = [i for i in query if i.lower() not in stopwords]
    return query

stop_words = set(stopwords.words('english'))  
stop_words = set([i.lower() for i in stop_words])
ps = PorterStemmer()
f = "merged.txt"
wp = wordPos(f)

while True:
    start = time.time()
    query = input ("Enter you query: ")
    oq = query
    query = word_tokenize(query)
    query = stopWord(query,stop_words)
    query = set([str((ps.stem(key.lower())).encode("utf-8")) for key in query])
    with open(f,"r",encoding = "utf-8") as file1:
        result = tfidf(query,wp,file1)

    print("\nThe top 10 URLs for {} are:\n".format(oq))
    for id in result.keys():
        print(doc_id[id])

    end = input("\nEnter C to continue search, and E to exit: ")
    print()
    if end == 'C':
        token_freq = {}
        token_post = {}
    if end == "E":
        break

    #print(time.time() - start)


