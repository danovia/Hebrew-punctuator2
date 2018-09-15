#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Should pass 1 parameter: <input_dir>"
	exit 1
fi

cat $1/*.txt | awk '{ print $2 }' | paste -sd " " - | sed 's/  /\n/g' \
	| shuf \
	| grep -x '.\{5,\}' \
	| grep -v " '[^ ]"
