**[Functional flow diagram](https://docs.google.com/drawings/d/15K7t3t4nmjn9XEa415ckmr0tjnJjgGW5N7KFRiXZEx4/edit?usp=sharing)**

# Hebrew-Wikipedia morphemes embeddings preparation
##### Note: This code is for Hebrew.

1. Download hebrew dataset from wikipedia to wikipedia-embeddings directory:
    - `cd Hebrew-punctuator2/Data-preparation/wikipedia-embeddings`
    - `wget https://dumps.wikimedia.org/hewiki/latest/hewiki-latest-pages-articles.xml.bz2`

2. `pip install --upgrade gensim` (https://radimrehurek.com/gensim/install.html)

3. `python3 wiki-XML-to-text.py`
    - It will create `wiki.he.text`

4. `bash split-wiki-to-10-parts.sh`
    - It splits Wikipedia to 10 parts for parallel parsing

5. `cd ./hebdepparser-dir; bash get-hebdepparser.sh`
    - It will download HebDepParser, and replace certain files where editted for parallel run.

6. Run in each directory from 0 to 9 the script `bash wiki-text-to-morphemes.sh`
    - You can see the script running in the parser-xa*.log file.
    - It may take 2-3 days for a high-end server to finish this task.

7. `bash merge-and-filter-10-wiki-parts.sh`
    - It should create the files `wiki-he-morph-0.txt` to `wiki-he-morph-9.txt` and `wiki-he-morph-FULL.txt`.

8. `python3 fasttxt.py`
    - It should create the files:
      - `wiki.he-morph.fasttext.skipgram-model.vec`
      - `wiki.he-morph.fasttext.CBOW-model.vec`
    - Those files are your embddings, enjoy!

# Citing
- Based on **[wordembedding-hebrew by liorshk](https://github.com/liorshk/wordembedding-hebrew)**.
- Uses **[HebDepParser](https://www.cs.bgu.ac.il/~yoavg/software/hebparsers/hebdepparser/)** by Yoav Goldberg, certain files where editted for parallel run, see them in ./hebdeparser/hebdepparser_editted_files .
