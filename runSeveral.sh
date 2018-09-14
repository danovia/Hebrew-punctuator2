#!/bin/bash
# Grid params
LR_ARRAY=(0.02)
HIDDEN_ARRAY=(256 512)
IS_ONE_WAY_ARRAY=(0 1)

# Other params
OUTPUT_DIR=testResults
INPUT_FILE=./example/out/ep.dev.txt

# Begin code:
mkdir $OUTPUT_DIR

TEMP_OUTPUT_FILE=temp_model_output.txt
MODEL_NAME=morphTest

for LR in ${LR_ARRAY[*]}; do
	for HIDDEN in ${HIDDEN_ARRAY[*]}; do
	    for IS_ONE_WAY in ${IS_ONE_WAY_ARRAY[*]}; do
            TEST_NAME=h${HIDDEN}_lr${LR}$([ "$IS_ONE_WAY" = 1 ] && echo "_oneWay" || echo "")
            TEMP_MODEL_FILE=Model_${MODEL_NAME}_${TEST_NAME}.pcl

            echo start training $TEST_NAME
            python main.py $MODEL_NAME $HIDDEN $LR $IS_ONE_WAY

            echo start testing $TEST_NAME
            python punctuator.py $TEMP_MODEL_FILE $TEMP_OUTPUT_FILE < $INPUT_FILE

            echo compute error for $TEST_NAME
            python error_calculator.py $INPUT_FILE $TEMP_OUTPUT_FILE > ${OUTPUT_DIR}/test_results_${TEST_NAME}.txt

            rm $TEMP_MODEL_FILE
        done
	done
done

rm $TEMP_OUTPUT_FILE
