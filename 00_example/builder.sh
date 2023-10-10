#!/bin/sh
while read rows
do
  wget -q $rows
done < /builder/jars.txt
