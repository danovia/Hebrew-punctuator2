import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

def train():

    # Model 1 - create morpheme-embeddings
    start = time.time()
    print(start)
    inp1 = "../wiki-he-morph-FULL.txt"
    out_model1 = "./wiki.he-morph.window10.word2vec.skipgram-model"
    model1 = Word2Vec(LineSentence(inp1), sg = 1, # 0=CBOW , 1= SkipGram
                     size=100, window=10, min_count=5, workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use (much) less RAM
    model1.init_sims(replace=True)
    print(time.time()-start)
    model1.save(out_model1)
    model1.wv.save_word2vec_format(out_model1+'.vec', binary=False)

    # Model 2 - create word-embeddings
    start = time.time()
    inp2 = "../wiki.he.text"
    out_model2 = "./wiki.he-regular.window5.word2vec.skipgram-model"
    model2 = Word2Vec(LineSentence(inp2), sg = 1, # 0=CBOW , 1= SkipGram
                     size=100, window=5, min_count=5, workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use (much) less RAM
    model2.init_sims(replace=True)
    print(time.time()-start)
    model2.save(out_model2)
    model2.wv.save_word2vec_format(out_model2+'.vec', binary=False)

def getModel(model = "wiki.he.word2vec.model"):

    model = Word2Vec.load(model)

    return model

if __name__ == '__main__':
    train()
