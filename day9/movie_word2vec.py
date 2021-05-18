from gensim.models import word2vec
import os

wData = word2vec.LineSentence('allMovie.nlp')
if os.path.isfile('movie_embedding.model'):
    model = word2vec.Word2Vec.load('movie_embedding.model')
    print(model.wv.most_similar(positive=['미나리']))
    print(model.wv.most_similar(positive=['재미'], negative=['노잼']))
else:
    model = word2vec.Word2Vec(wData,
                              sg=1,
                              vector_size=200,
                              window=3,
                              min_count=3,
                              workers=4)
    model.save('movie_embedding.model')