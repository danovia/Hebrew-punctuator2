#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Should pass 1 parameter: <concat_morphemes> (either 0 or 1)"
	exit 1
fi

rm -rf ./out

echo "Step 1/3"
mkdir ./out

cat /dev/stdin > step1.txt
	
echo "Step 2/3"

python dont_run_me_run_the_other_script_instead.py step1.txt step2.txt $1

echo "Step 3/3"

./splitpercs.sh step2.txt 80 10 10

mv part00 out/ep.train.txt
mv part01 out/ep.dev.txt
mv part02 out/ep.test.txt

echo "Cleaning up..."

rm -f step1.txt step2.txt step3.txt

echo "Preprocessing done. Now you can give the produced ./out dir as <data_dir> argument to data.py script for conversion and continue as described in the main README.md"
