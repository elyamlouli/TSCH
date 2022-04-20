#!/usr/bin/bash 

if [ "$#" -ne "4" ]; then
    echo "batch_compile.sh <delai_start> <delai_end> <seed_start> <seed_end>";
    exit 1;
fi

delai_start=$1
delai_end=$2
seed_start=$3
seed_end=$4

cd ../src/
dir="../firmwares"
mkdir -p $dir

for seed in $(seq $seed_start $seed_end)
do
    for delai in $(seq $delai_start $delai_end)
    do 
        ./compile.sh $seed $delai
        cp ./sender.iotlab $dir/sender-$delai-$seed.iotlab
        cp ./simple-sender.iotlab $dir/simple-sender-$delai.iotlab
    done
done
