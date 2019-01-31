#! /bin/bash

while [ 1 ]
do
NAME=$(ls | grep -v -e '\.zip$' -e 'orig' -e 'unzip.sh')

mv $NAME pass.zip
unzip pass.zip
echo "$NAME"

done
