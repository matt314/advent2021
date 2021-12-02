#!/bin/zsh -
# I'm fully aware of how silly but not as inefficient this is compared to the last one

file=foo.txt

line="0"
increase="0"
totlines=$(wc -l $file | awk '{print $1;};')

echo "Read $file into array"
a_ray=($(cat $file))

line=3
while test $line -lt $totlines ; do
  curr=$[${a_ray[$line]} + ${a_ray[$[$line-1]]} + ${a_ray[$[$line-2]]}]
  prev=$[${a_ray[$[$line-1]]} + ${a_ray[$[$line-2]]} + ${a_ray[$[$line-3]]}]

#  echo curr $curr prev $prev
  # bigger?
  if test $curr -gt $prev ; then
    increase=$[$increase + 1]
  fi
  line=$[$line + 1]
done

echo Lines: $line
echo Increases: $increase

exit
