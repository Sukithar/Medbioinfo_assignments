#!/bin/bash
#script to download alignment software and
#to do alignment on all files in a folder
#
#created: June 02, 2017
#Sukithar Rajan
##########################################

#open the working folder for reading files and software
DATA="/Users/srrn/Desktop/Practise/MedBioinfo/yeast_genes/"
SRC="/Users/srrn/Desktop/Practise/MedBioinfo/"

cd $SRC
#check if alignment software is present
file="${SRC}muscle"
if [ -f "$file" ]
then
    echo "$file exists"
else
    echo "Please download the software !"
fi

cd $DATA
file='test*'
#f1=0
#read every file in the folder 1 by 1 and list gene families
for i in $file ;
  do
    echo $i
    for j in $(cat $i | grep ">" | cut -c 1-5| head -5);
    	do
    	echo $j
	    ${SRC}muscle -in $j -out $j.muscle.test
		done
  done
