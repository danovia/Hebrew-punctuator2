**[Functional flow diagram](https://docs.google.com/drawings/d/15K7t3t4nmjn9XEa415ckmr0tjnJjgGW5N7KFRiXZEx4/edit?usp=sharing)**

# Hebrew morpheme-embeddings generation
##### TLDR: already trained morpheme-embeddings can be found in `./fasttext`. 

1. Download hebrew dataset from Wikipedia to wikipedia-embeddings directory:
    - `cd Hebrew-punctuator2/Data-preparation/wikipedia-embeddings`
    - `wget https://dumps.wikimedia.org/hewiki/latest/hewiki-latest-pages-articles.xml.bz2`

2. `pip install --upgrade gensim` (https://radimrehurek.com/gensim/install.html)

3. `python3 wiki-XML-to-text.py`
    - It will create `wiki.he.text`

4. `bash split-wiki-to-10-parts.sh`
    - It splits Wikipedia to 10 parts for parallel parsing

5. `cd ./hebdepparser-dir; bash get-hebdepparser.sh`
    - It will download HebDepParser, and replace certain files editted for parallel run.

6. Run in each directory from 0 to 9 the script `wiki-text-to-morphemes.sh`
    - You can monitor the process in it's log file.
    - It may take 2-3 days for a high-end server to finish this task.

7. `cd ..; bash merge-and-filter-10-wiki-parts.sh`
    - It should create the files `wiki-he-morph-0.txt` to `wiki-he-morph-9.txt` and `wiki-he-morph-FULL.txt`.

8. `cd fasttext; python3 fasttxt.py`
    - It should create the file:
      - `wiki.he-morph.fasttext.skipgram-model.vec`
    - This is the morpheme-embeddings file, enjoy!


# Acknowledgements
* Based on **[wordembedding-hebrew](https://github.com/liorshk/wordembedding-hebrew)** by liorshk.
* Uses **[HebDepParser](https://www.cs.bgu.ac.il/~yoavg/software/hebparsers/hebdepparser/)** by Yoav Goldberg, certain files where editted for parallel run, see them in `./hebdeparser-dir/hebdepparser_editted_files` .
