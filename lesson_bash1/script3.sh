#!/bin/bash
ls -1
FILE_COUNT=$(ls -1 | wc -l)
echo "Total number of files: $FILE_COUNT"
