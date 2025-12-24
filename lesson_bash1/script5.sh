#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Error: You must provide exactly two arguments."
    exit 1
fi
MODE=$1
INPUT=$2
if [ "$MODE" == "crypt" ]; then
    echo "Encrypting..."
    echo -n "$INPUT" | base64
elif [ "$MODE" == "decrypt" ]; then
    echo "Decrypting..."
    echo -n "$INPUT" | base64 --decode
else
    echo "Error: Invalid mode. Use 'crypt' or 'decrypt'."
    exit 1
fi