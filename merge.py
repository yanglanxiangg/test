import time


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

wp1 = wordPos("-posting1.txt")
wp2 = wordPos("-posting2.txt")
wp3 = wordPos("-posting3.txt")
wp4 = wordPos("-posting4.txt")


def mergeFiles(wp1,wp2,wp3,wp4,file1,file2,file3,file4,merged):
    visited = set()
    for token in wp1.keys():
        if token not in visited:
            pos = wp1[token]
            file1.seek(pos)
            line = file1.readline()
            line = line.split("----")
            freq = int(line[1])
            post = eval(line[2])
            if token in wp2:
                pos = wp2[token]
                file2.seek(pos)
                line = file2.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp3:
                pos = wp3[token]
                file3.seek(pos)
                line = file3.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp4:
                pos = wp4[token]
                file4.seek(pos)
                line = file4.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            s = token + "----" + str(freq) + "----" + str(post) + '\n'
            merged.write(s)
            visited.add(token)

    for token in wp2.keys():
        if token not in visited:
            pos = wp2[token]
            file2.seek(pos)
            line = file2.readline()
            line = line.split("----")
            freq = int(line[1])
            post = eval(line[2])
            if token in wp1:
                pos = wp1[token]
                file1.seek(pos)
                line = file1eadline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp3:
                pos = wp3[token]
                file3.seek(pos)
                line = file3.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp4:
                pos = wp4[token]
                file4.seek(pos)
                line = file4.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            s = token + "----" + str(freq) + "----" + str(post) + '\n'
            merged.write(s)
            visited.add(token)

    for token in wp3.keys():
        if token not in visited:
            pos = wp3[token]
            file3.seek(pos)
            line = file3.readline()
            line = line.split("----")
            freq = int(line[1])
            post = eval(line[2])
            if token in wp2:
                pos = wp2[token]
                file2.seek(pos)
                line = file2.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp1:
                pos = wp1[token]
                file1.seek(pos)
                line = file1.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp4:
                pos = wp4[token]
                file4.seek(pos)
                line = file4.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            s = token + "----" + str(freq) + "----" + str(post) + '\n'
            merged.write(s)
            visited.add(token)

    for token in wp4.keys():
        if token not in visited:
            pos = wp4[token]
            file4.seek(pos)
            line = file4.readline()
            line = line.split("----")
            freq = int(line[1])
            post = eval(line[2])
            if token in wp2:
                pos = wp2[token]
                file2.seek(pos)
                line = file2.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp3:
                pos = wp3[token]
                file3.seek(pos)
                line = file3.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            if token in wp1:
                pos = wp1[token]
                file1.seek(pos)
                line = file1.readline()
                line = line.split("----")
                freq += int(line[1])
                #post.extend(eval(line[2]))
                post.update(eval(line[2]))
            s = token + "----" + str(freq) + "----" + str(post) + '\n'
            merged.write(s)
            visited.add(token)

def mergeDoc(file1,file2,file3,file4,merged):
    lines = file1.readlines()
    for line in lines:
        if "http://" in line:
            line = line.replace("http://","https://")
        merged.write(line)
    lines = file2.readlines()
    for line in lines:
        if "http://" in line:
            line = line.replace("http://","https://")
        merged.write(line)
    lines = file3.readlines()
    for line in lines:
        if "http://" in line:
            line = line.replace("http://","https://")
        merged.write(line)
    lines = file4.readlines()
    for line in lines:
        if "http://" in line:
            line = line.replace("http://","https://")
        merged.write(line)


            

with open("-posting1.txt","r",encoding='utf-8',) as file1, open("-posting2.txt","r",encoding='utf-8',) as file2, open("-posting3.txt","r",encoding='utf-8',) as file3, open("-posting4.txt","r",encoding='utf-8',) as file4, open("merged.txt","w",encoding='utf-8',) as merged:
    start_time = time.time()
    mergeFiles(wp1,wp2,wp3,wp4,file1,file2,file3,file4,merged)
    print(time.time() - start_time)

with open("-docid1.txt","r",encoding='utf-8',) as file1, open("-docid2.txt","r",encoding='utf-8',) as file2, open("-docid3.txt","r",encoding='utf-8',) as file3, open("-docid4.txt","r",encoding='utf-8',) as file4, open("mergedDocid.txt","w",encoding='utf-8',) as merged:
    start_time = time.time()
    mergeDoc(file1,file2,file3,file4,merged)
    print(time.time() - start_time)