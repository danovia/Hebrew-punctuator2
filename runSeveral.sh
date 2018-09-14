#!/bin/bash

RESULTS_DIR=./results
EVALUATIONS_DIR=${RESULTS_DIR}/evaluations
MODELS_DIR=${RESULTS_DIR}/models
OUTPUTS_DIR=${RESULTS_DIR}/outputs

INPUT_FILE=./example/out/ep.dev.txt

# Begin code:
mkdir $EVALUATIONS_DIR
mkdir $MODELS_DIR
mkdir $OUTPUTS_DIR

function run_data() {
    local embeddings=$1
    local produce_data_cmd=$2

    rm We.pcl
    rm -rf transformed_data

    eval $produce_data_cmd | ./example/generate_final_dataset.sh 0

    python data.py --stage1=./example/out --embed=$embeddings
}

function run_model() {
    local hidden=$1
    local lr=$2
    local isOneWay=$3
    local model_name=$4

    local model_substr=h${hidden}_lr${lr}$([ "$isOneWay" = 1 ] && echo "_oneWay" || echo "")
    local evaluation_file=${EVALUATIONS_DIR}/Evaluation_${model_name}_${model_substr}.txt
    local model_file=${MODELS_DIR}/Model_${model_name}_${model_substr}.pcl
    local output_file=${OUTPUTS_DIR}/Output_${model_name}_${model_substr}.txt

    python main.py $model_name $hidden $lr $isOneWay
    python punctuator.py $model_file $output_file < $INPUT_FILE
    python error_calculator.py $INPUT_FILE $output_file > $evaluation_file
}

run_data ./example/embeddings/wiki.he-morph.window10.fasttext.skipgram-model.vec "./example/convert_table_dataset.sh ./example/training-hebrew/ | python ./example/untransliterate.py"
run_model 512 0.02 0 morph_fasttext10
