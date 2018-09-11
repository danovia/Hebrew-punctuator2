#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Should pass 1 parameter: <input_dir>"
	exit 1
fi

cat $1/*.txt | awk '{ print $2 }' | paste -sd " " - | sed 's/  /\n/g' \
	| shuf \
	| sed 's/[ ]*yyCM/,/g;
		   s/[ ]*yyCLN/:/g;
		   s/yyLRB[ ]*/(/g;
		   s/yyQUOT/"/g;
		   s/[ ]*yyDOT/./g;
		   s/yyDASH/-/g;
		   s/[ ]*yyRRB/)/g;
		   s/[ ]*yyEXCL/!/g;
		   s/[ ]*yyQM/?/g;
		   s/[ ]*yySCLN/;/g;
		   s/[ ]*yyELPS/.../g;
		   s/@suf/suf/g' \
	| grep -x '.\{5,\}' \
	| grep -v " '[^ ]"
