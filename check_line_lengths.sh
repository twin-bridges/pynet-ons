#!/bin/bash
# Excludes show_*.txt command output from network devices
MY_FILES=`find . -name '*.txt' | grep -v 'show_.*.txt'`
OUTPUT=`grep -l '.\{100\}' $MY_FILES`

echo
if [ "$OUTPUT" != "" ]; then
    echo "Text files longer than 100 chars detected:"
    echo $OUTPUT
    echo
    exit 1
else
    echo "Text files all good!"
    echo
    exit 0
fi

#grep -l '.\{100\}' `find . -name '*.txt' | grep -v 'show_.*.txt'`
