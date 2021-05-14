# pip install gensim
import requests
from gensim.models.word2vec import Word2Vec
res = requests.get("https://www.gutenberg.org/files/2591/2591-0.txt")
# 불필요한 단어 제거
grimm = res.text[2801:530661]
import re
grimm = re.sub(r'[^a-zA-Z\.]', ' ', grimm)
# 문장 단위로 자르기
sentences = grimm.split('. ')
data = [s.split() for s in sentences]
print(data[0])

model = Word2Vec(data
                ,sg=1 #0 : CBOW 1:skip-gram
                ,vector_size=100
                ,window=3
                ,min_count=3
                ,workers=4)
model.save('first_embedding_model')