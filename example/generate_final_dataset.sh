#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Should pass 1 parameter: <concat_morphemes> (either 0 or 1)"
	exit 1
fi

DIR=`dirname "$0"`

rm -rf ${DIR}/out

echo "Step 1/3"
mkdir ${DIR}/out

cat /dev/stdin > ${DIR}/step1.txt
	
echo "Step 2/3"

python ${DIR}/dont_run_me_run_the_other_script_instead.py ${DIR}/step1.txt ${DIR}/step2.txt $1

echo "Step 3/3"

${DIR}/splitpercs.sh ${DIR}/step2.txt 80 10 10

mv part00 ${DIR}/out/ep.train.txt
mv part01 ${DIR}/out/ep.dev.txt
mv part02 ${DIR}/out/ep.test.txt

echo "Cleaning up..."

rm -f ${DIR}/step1.txt ${DIR}/step2.txt ${DIR}/step3.txt

echo "Preprocessing done. Now you can give the produced ./out dir as <data_dir> argument to data.py script for conversion and continue as described in the main README.md"
