#!/usr/bin/bash

if [ "$#" -lt "2" ]; then
    echo "run <seed> <delai>"
    exit 1;
fi

seed=$1
delai=$2

echo "
#ifndef DEFINE_H
#define DEFINE_H

#define SEED $seed
#define DELAI $delai * CLOCK_SECOND

#endif
" > define.h

ARCH_PATH=../../iot-lab/parts/iot-lab-contiki-ng/arch make TARGET=iotlab BOARD=m3 savetarget
ARCH_PATH=../../iot-lab/parts/iot-lab-contiki-ng/arch make distclean
ARCH_PATH=../../iot-lab/parts/iot-lab-contiki-ng/arch make clean
ARCH_PATH=../../iot-lab/parts/iot-lab-contiki-ng/arch make
