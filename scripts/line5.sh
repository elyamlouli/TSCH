#!/usr/bin/bash 

if [ "$#" -ne "3" ]; then
    echo "line5.sh <delai> <seed_start> <seed_end>";
    exit 1;
fi

delai=$1
seed_start=$2
seed_end=$3

firmware_path="../firmwares"
path="../output"

sender_nodes="53+55+59+61"
coordinator_node="57"


mkdir -p $path

for seed in $(seq $seed_start $seed_end)
do
    name="$delai-$seed"
    res=$(iotlab-experiment submit -n line5-$name -d 20 -l "strasbourg,m3,$sender_nodes,$firmware_path/sender-$name.iotlab" -l "strasbourg,m3,$coordinator_node,$firmware_path/coordinator-$name.iotlab") 
    iotlab-experiment wait 
    id=$(echo "$res" | sed -n -e '2{p;q}' | cut -f2 -d":")
    serial_aggregator -i $id > $path/line5-$name.txt
done

