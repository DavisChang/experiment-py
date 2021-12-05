#encoding=utf-8

import jieba
from os import listdir
from os.path import isfile, join

# Support Traditional Chinese
jieba.set_dictionary('./dict.txt.big')

mypath = './News'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print('onlyfiles:', onlyfiles)


news_string = ''
for filename in onlyfiles:
    print()
    with open(f'./News/{filename}', encoding='utf-8', mode='r') as rf:
    	for l in rf:
    		news_string += l.strip()
print('news_string:', len(news_string))


# cut string
jieba_result = jieba.cut(news_string, cut_all=False, HMM=True)

# words
with open('./NTUSD_positive_unicode.txt', encoding='utf-8', mode='r') as f:
    positive_words = []
    for l in f:
        positive_words.append(l.strip())
 
with open('./NTUSD_negative_unicode.txt', encoding='utf-8', mode='r') as f:
    negative_words = []
    for l in f:
        negative_words.append(l.strip())

print('positive_words:', len(positive_words))
print('negative_words:', len(negative_words))

score = 0
for word in jieba_result:
    if word in positive_words:
        score += 1
        print(f'目前詞彙:{word}, 總分:{score}')
    elif word in negative_words:
        score -= 1
        print(f'目前詞彙:{word}, 總分:{score}')
    else:
      pass