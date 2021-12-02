#!/bin/zsh -
#
# I'm fully aware of how silly and inefficient this is

file=foo.txt

line="1"
increase="0"
old=$(head -n 1 $file)
totlines=$(wc -l $file | awk '{print $1;};')

while test $line -lt $totlines ; do
  line=$[$line + 1]
  curr=$(head -n $line $file | tail -n 1)

  # bigger?
  if test $curr -gt $old ; then
    increase=$[$increase + 1]
  fi

  old=$curr
done

echo
echo Lines: $line
echo Increases: $increase

exit
