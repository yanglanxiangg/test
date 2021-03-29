import os
import sys
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import math



path = r"C:\Users\Lanxiang Yang\source\repos\CS121Assignment2M2\CS121Assignment2M2\DEV"

file = []
for root, directories, files in os.walk(path):
	for name in files:
		file.append(os.path.join(root, name))

def write_to_disk(f1,f2):
    with open(f1,'a',encoding = 'utf-8') as report:
        for key in token_freq.keys():
            #str(key.encode("utf-8"))
            d = {k: v for k, v in sorted(token_post[key].items(), key=lambda item: item[1][0], reverse = True)}
            s = str(key.encode("utf-8")) + "----" + str(token_freq[key]) + "----" + str(d) + '\n'
            report.write(s)

    with open(f2,'a',encoding = 'utf-8') as report:
        for key in doc_id.keys():
            s = str(key) + '----' + str(doc_id[key])
            report.write(s + '\n')

files = file
urls = set()
token_freq = {}
token_post = {}
token_ = {}
doc_id = {}
doc_id_count = 0
count = 0
round = 1
ps = PorterStemmer()
# Tracking data
t_count = 0
count2 = 0
for file in files:
    with open(file,'r') as read_file:
        data = json.load(read_file)
 
    url = data['url']
    parsed = urlparse(url)
    url = parsed.scheme + "://"+parsed.netloc + parsed.path + parsed.params + parsed.query
    if url not in urls:
        #Tracking
        t_count += 1
        print(t_count)
        count += 1
        print(file) 
        urls.add(url)
        soup = BeautifulSoup(data['content'], 'html.parser')
        # Important text
        important_tags = soup.find_all([ 'b', 'strong', 'h1', 'h2', 'h3','title'], text=True)
        important_text = ' '.join([tag.string for tag in important_tags])
        important_text = word_tokenize(important_text)
        important_text = [ps.stem(word.lower()) for word in important_text if (word.isalnum() and len(word) > 1)]
        # Remove Noise
        tags = soup.find_all(['a','script','style','tr'])
        for tag in tags:
            tag.extract()
        # Get text
        text = soup.get_text(separator = '\n')
        text.encode('utf-8')
        words = text.split('\n')
        # Handling npy files
        if url.endswith(".npy"):
            words = words[0]
            token_words = word_tokenize(words)
            tokens = [ps.stem(word.lower()).lower() for word in token_words if word.isalnum()]
            tokens_norep = set(tokens)
            for token in tokens_norep:
                if token not in token_freq.keys():
                    token_freq[token] = 1
                else:
                    token_freq[token] += 1
                if token not in token_post.keys():
                    token_post[token] = {}
                    token_post[token][doc_id_count] = []
                    token_post[token][doc_id_count].append(tokens.count(token))
                    token_post[token][doc_id_count].append(0)
                else:
                    token_post[token][doc_id_count] = []
                    token_post[token][doc_id_count].append(tokens.count(token))
                    token_post[token][doc_id_count].append(0)
        else:
            tokens = list()
            for i in words:
                token_words = word_tokenize(i)
                tokens.extend([ps.stem(word.lower()) for word in token_words if (word.isalnum() and len(word) > 1)])
            tokens_norep = set(tokens)
            for token in tokens_norep:
                if token not in token_freq.keys():
                    token_freq[token] = 1
                else:
                    token_freq[token] += 1
                if token not in token_post.keys():
                    token_post[token] = {}
                    token_post[token][doc_id_count] = []
                    token_post[token][doc_id_count].append(tokens.count(token))

                    token_post[token][doc_id_count].append(0)

                else:
                    token_post[token][doc_id_count] = []
                    token_post[token][doc_id_count].append(tokens.count(token))
                    token_post[token][doc_id_count].append(0)
        for token in important_text:
            if token in tokens_norep:
                token_post[token][doc_id_count][1] += (1 + math.log10(1.2/10))

        doc_id[doc_id_count] = url
        doc_id_count += 1

    # 13448
    if count == 13448:
        netloc = parsed.netloc
        new_urls = set([i for i in urls if netloc in i])
        urls = new_urls
        if round == 1:
            write_to_disk("-posting1.txt","-docid1.txt")
        elif round == 2:
            write_to_disk("-posting2.txt","-docid2.txt")
        elif round == 3:
            write_to_disk("-posting3.txt","-docid3.txt")
        elif round == 4:
            write_to_disk("-posting4.txt","-docid4.txt")
        print("-----------Writing to disk-----------")
        print("Before Cleaning Size:")
        print(sys.getsizeof(token_post) + sys.getsizeof(token_freq) + sys.getsizeof(doc_id))
        token_freq = {}
        token_post = {}
        doc_id = {}
        count2 += count
        count = 0
        round += 1
        print("After Cleaning Size:")
        print(sys.getsizeof(token_post) + sys.getsizeof(token_freq) + sys.getsizeof(doc_id))

print(count2)