import json
import jieba


# 获取停用词列表
def getStopwords():
    stopwords = [line.strip() for line in open('baidu_stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords

# 使用精确模式分词
def splitWords():
    txt = open("contents.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    return words

# 去除停用词
def movStopwords(stopWords, words):
    lists = []
    for word in words:
        if word not in stopWords:
            lists.append(word)
    return lists

# 格式转化
def format(words):
    counts = {}
    formatStr = []
    temp = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for name, value in items:
        if value > 50:
            temp["name"] = name
            temp["value"] = value
            formatStr.append(temp)
            temp = {}
    return formatStr

# 保存分词后的json文件
def save(fotmatList):
    jsonStr = json.dumps(fotmatList, indent=4)
    with open("word.json", "a+", encoding="utf-8") as f:
        f.write(jsonStr)

def main():
    stopWords = getStopwords()
    words = splitWords()
    # print(len(words))
    words = movStopwords(stopWords, words)
    # print(len(words))
    fotmatList = format(words)
    # print(fotmatStr)
    save(fotmatList)        

main()
