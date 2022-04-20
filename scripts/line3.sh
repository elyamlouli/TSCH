#!/usr/bin/bash 

if [ "$#" -ne "3" ]; then
    echo "line3.sh <delai> <seed_start> <seed_end>";
    exit 1;
fi

delai=$1
seed_start=$2
seed_end=$3

path="../output"

sender_nodes="54+58"
coordinator_node="56"


mkdir -p $path

for seed in $(seq $seed_start $seed_end)
do
    name="$delai-$seed"
    res=$(iotlab-experiment submit -n line3-$name -d 20 -l "strasbourg,m3,$sender_nodes,../firmwares/sender-$name.iotlab" -l "strasbourg,m3,$coordinator_node,../src/coordinator.iotlab") 
    iotlab-experiment wait 
    id=$(echo "$res" | sed -n -e '2{p;q}' | cut -f2 -d":")
    serial_aggregator -i $id > $path/line3-$name.txt
done

