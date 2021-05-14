from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('first_embedding_model')
# 단어를 벡터로 변환
print(model.wv['princess'])
# 두단어의 유사성 비교
print(model.wv.similarity('princess', 'queen'))
# 유사한 단어
print(model.wv.most_similar('princess'))
#


