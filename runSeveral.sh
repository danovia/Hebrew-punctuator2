#!/bin/bash

RESULTS_DIR=./results
EVALUATIONS_DIR=${RESULTS_DIR}/evaluations
OUTPUTS_DIR=${RESULTS_DIR}/outputs

INPUT_FILE=./example/out/ep.dev.txt

# Begin code:
mkdir $EVALUATIONS_DIR
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
    local model_file=Model_${model_name}_${model_substr}.pcl
    local output_file=${OUTPUTS_DIR}/Output_${model_name}_${model_substr}.txt

    python main.py $model_name $hidden $lr $isOneWay
    python punctuator.py $model_file $output_file < $INPUT_FILE
    python error_calculator.py $INPUT_FILE $output_file > $evaluation_file
}

function run_baseline() {
    local gramsBefore=$1
    local gramsAfter=$2

    local evaluation_file=${EVALUATIONS_DIR}/Evaluation_baseline_${gramsBefore}before_${gramsAfter}after.txt

    python baseline.py $gramsBefore $gramsAfter > $evaluation_file
}

#run_data ./example/embeddings/wiki.he-morph.window10.fasttext.skipgram-model.vec "./example/convert_table_dataset.sh ./example/training-hebrew-morph/ | python ./example/untransliterate.py"
#run_model 512 0.02 0 morph_fasttext10
#run_model 256 0.02 0 morph_fasttext10
#run_model 256 0.02 1 morph_fasttext10
#run_data ./example/embeddings/wiki.he-morph.window10.word2vec.skipgram-model.vec "./example/convert_table_dataset.sh ./example/training-hebrew-morph/ | python ./example/untransliterate.py"
#run_model 512 0.02 0 morph_word2vec10
#run_data ./example/embeddings/wiki.he-regular.window5.fasttext.skipgram-model.vec "cat ./example/training-hebrew-full/*.txt"
#run_model 512 0.02 0 full_fasttext5
#run_data ./example/embeddings/wiki.he-regular.window5.word2vec.skipgram-model.vec "cat ./example/training-hebrew-full/*.txt"
#run_model 512 0.02 0 full_word2vec5

#run_baseline 1 1
#run_baseline 1 2
#run_baseline 2 1
#run_baseline 2 0
#run_baseline 0 2
