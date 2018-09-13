#!/bin/bash
HEBDEPARSER_DIR="./hebdepparser-dir/hebdepparser"
WIKI_FILE="`pwd`/`ls | grep xa | grep -v log`"
WIKI_LINE_READ_OFFSET=0
PORT=$((8080 + `basename "$PWD"`))
mkdir he-morph-new

echo "Starting java server..."
kill -9 `ps -ef | grep "${TAGGER_DIR}/tagger_server_bm_lemma.jar ${PORT}" | grep -v grep | awk '{print $2}'`
TAGGER_DIR="${HEBDEPARSER_DIR}/tagger/tagger_server"
java -Xmx1200m -XX:MaxPermSize=256m -server -jar "${TAGGER_DIR}/tagger_server_bm_lemma.jar" ${PORT} "${TAGGER_DIR}/tagger_data/" pretokenize noChunk noNER &
sleep 20

echo "Starts parsing wiki articles:"
kill -9 `ps -ef | grep "python2.7 parse.py $WIKI_LINE_READ_OFFSET $PORT" | grep -v grep | awk '{print $2}'`
cat "${WIKI_FILE}" | python2.7 ${HEBDEPARSER_DIR}/parse.py $WIKI_LINE_READ_OFFSET $PORT &>> "parser-`ls | grep xa | grep -v log`.log" &
less +F "parser-`ls | grep xa | grep -v log`.log"

echo "Finished initilization, see parser-`ls | grep xa | grep -v log`.log for more information."
