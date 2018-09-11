#!/bin/bash
# Grid params
LR_ARRAY=(0.01 0.02 0.04)
HIDDEN_ARRAY=(64 128 256 512)

# Other params
OUTPUT_DIR=testResults
INPUT_FILE=./example/out/ep.dev.txt

# Begin code:
mkdir $OUTPUT_DIR

TEMP_OUTPUT_FILE=temp_model_output.txt
MODEL_NAME=temp_test

for LR in ${LR_ARRAY[*]}; do
	for HIDDEN in ${HIDDEN_ARRAY[*]}; do
		TEST_NAME=h${HIDDEN}_lr${LR}
		TEMP_MODEL_FILE=Model_${MODEL_NAME}_${TEST_NAME}.pcl
		
		echo start training $TEST_NAME
		python main.py $MODEL_NAME $HIDDEN $LR
		
		echo start testing $TEST_NAME
		python punctuator.py $TEMP_MODEL_FILE $TEMP_OUTPUT_FILE < $INPUT_FILE
		
		echo compute error for $TEST_NAME
		python error_calculator.py $INPUT_FILE $TEMP_OUTPUT_FILE > ${OUTPUT_DIR}/test_results_${TEST_NAME}.txt
		
		rm $TEMP_MODEL_FILE
	done
done

rm $TEMP_OUTPUT_FILE
