#! /bin/bash

while [ 1 ]
do
NAME=$(ls | grep -v -e '\.zip$' -e 'orig' -e 'unzip.sh' -e 'unxz.sh' -e '\.xz$' -e '\.bz2' -e 'unbz.sh')

mv $NAME pass.bz2
bzip2 -d pass.bz2
echo "$NAME"

done
