#!/bin/bash
PARAM=$1
if [ -d "$PARAM" ]; then
    echo "$PARAM - dir"
elif [ -f "$PARAM" ]; then
    echo "$PARAM - file"
else
    echo "$PARAM - not exist"
fi
