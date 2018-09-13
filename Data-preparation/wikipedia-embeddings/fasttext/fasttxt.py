import fasttext
import time

def train():
    inp = "../wiki-he-morph-FULL.txt"
    skipgram_out_model = "./wiki.he-morph.fasttext.skipgram-model"
    cbow_out_model = "./wiki.he-morph.fasttext.cbow-model"

    start = time.time()
    print(start)

    # Skipgram model
    model = fasttext.skipgram(inp, skipgram_out_model)

    # CBOW model
    model = fasttext.cbow(inp, cbow_out_model)
    print(time.time()-start)

def getModel(model = "wiki.he.fasttext.model.bin"):

    model = fasttext.load_model(model)

    return model

if __name__ == '__main__':
    train()
