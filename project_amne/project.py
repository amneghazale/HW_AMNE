#part 1
def count_appearances(str):
    d={}
    d_keys = []
    for c in str.lower():
        if c.isalpha():
            if c in d_keys:
                d[c]+=1
            else:
                d[c]=1
                d_keys.append(c)
    return dict(sorted(d.items(),key=lambda x:x[1],reverse=True))

def create_dic(str):
    d_res ={}
    d_counts=count_appearances(str)

    keys =list(d_counts.keys())
    d_res['e']=keys[0]
    d_res['t'] = keys[1]
    d_res['o'] = keys[2]
    d_res['r'] = keys[3]

    d_res[keys[0]]='e'
    d_res[keys[1]] = 't'
    d_res[keys[2]] = 'o'
    d_res[keys[3]] = 'r'

    return d_res

#part 2
def decrypte_message(msg):
    res =list(msg.lower())
    dic = create_dic(msg)
    #dic={'a': 'e', 'c': 'o', 'b': 't', 'e': 'a', 'd': 'r', 'o': 'c', 'r': 'd', 't': 'b'}

    keys = list(dic.keys())
    for i in range(len(res)):
        if res[i].isalpha():
            if res[i].lower() in keys:
                res[i] = str(dic.get(res[i].lower()))

    return "".join(res)

#part 3
def encryptrFile(path):
    f = open(path,"r")
    msg = f.read()
    enc_msg = decrypte_message(msg)
    f = open(path, "a")
    f.write("\nThe encryption for the above text is:\n")
    f.write(enc_msg)
    f=open("results.txt","w")
    f.write(enc_msg)

#encryptrFile("est.txt")
#part 4
import re
regex=re.compile('[^a-zA-Z]')


def longest_words(path):
    list =[]
    f = open(path, "r")
    data = f.read().split()
    d = {}
    for word in data:
        word=regex.sub('',word)
        d[word]=len(word)
    d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
    d_keys=d.keys()
    for k in d_keys:
        max_length= len(k)
        break
    for word in data:
        word=regex.sub('',word)
        if max_length==len(word):
            list.append(word)

    return list

def count_lines(path):
    lines_count = 0
    with open (path,'r') as fp:
        lines_count=len(fp.readlines())
    return lines_count

def main():
    encryptrFile("est.txt")
    list = longest_words("results.txt")
    lines_num = count_lines("results.txt")
    f = open("est.txt", "a")
    f.write("\n")
    for i in range(lines_num):
        f.write(list[0]+" ")
    f.write("\n")

if __name__ == '__main__':
    main()
