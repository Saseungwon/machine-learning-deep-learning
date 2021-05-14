from gensim.models import word2vec
# 한국어 임베딩 파일
# https://github.com./kyubyong/wordvectors
kovec = word2vec.Word2Vec.load('ko.bin')
print(kovec.wv.most_similar('한국'))
# kovec.wv.most_similar(positive=['일본','서울'],negative=['한국'])