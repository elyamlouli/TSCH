#!/usr/bin/bash 

if [ "$#" -ne "1" ]; then
    echo "square.sh <delai>";
    exit 1;
fi

delai=$1
seed=1
path="../output"

#sender_nodes="1-6+19-22+29-33"
sender_nodes="5-10+21-24+33-37"

# coordinator_node="34"
coordinator_node="38"


mkdir -p $path

name="$delai-$seed"
res=$(iotlab-experiment submit -n square-$name -d 20 -l "strasbourg,m3,$sender_nodes,../firmwares/simple-sender-$name.iotlab" -l "strasbourg,m3,$coordinator_node,../src/coordinator.iotlab") 
iotlab-experiment wait 
id=$(echo "$res" | sed -n -e '2{p;q}' | cut -f2 -d":")
serial_aggregator -i $id > $path/square-$name.txt

