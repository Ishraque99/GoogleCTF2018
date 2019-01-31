#! /bin/bash

while [ 1 ]
do
NAME=$(ls | grep -v -e '\.zip$' -e 'orig' -e 'unzip.sh' -e 'unxz.sh' -e '\.xz$' -e '\.bz2' -e 'unbz.sh' -e 'ungz.sh' -e '\.gz$')

mv $NAME pass.gz
gzip -d pass.gz
echo "$NAME"

done
