#! /bin/bash

while [ 1 ]
do
NAME=$(ls | grep -v -e '\.zip$' -e 'orig' -e 'unzip.sh' -e 'unxz.sh' -e '\.xz$')

mv $NAME xz.xz
unxz xz.xz
echo "$NAME"

done
