import fasttext
import time

def train():
    inp = "../wiki-he-morph-FULL.txt"
    start = time.time()
    print(start)

    # We used Skipgram, should be better when not used for word prediction
    out_model = "./wiki.he-morph.fasttext.skipgram-model"
    model = fasttext.skipgram(inp, out_model, window=10, min_count=3)

    # CBOW model
    # out_model = "./wiki.he-morph.fasttext.cbow-model"
    # model = fasttext.cbow(inp, out_model, window=10, min_count=5)

    print(time.time()-start)

def getModel(model = "wiki.he-morph.fasttext.skipgram-model.bin"):

    model = fasttext.load_model(model)

    return model

if __name__ == '__main__':
    train()
