#!/bin/bash


##theoretically this is the only line you should need to change
MY_BIN_NUMBER="188"

#set up temp files and other variables for use in the script
MY_BIN_FILE="BIN_$MY_BIN_NUMBER.fa"
MY_BAM_FILE="IN01201_all_sorted.bam"
MY_INTERMEDIATE="$(mktemp)"
MY_INTERMEDIATE2="$(mktemp)"
MY_OUTPUT="BIN_$MY_BIN_NUMBER.reads.pairs.fq.gz"
MY_OUTPUT2="BIN_$MY_BIN_NUMBER.reads.singles.fq.gz"

#Grab each contig name from the GroopM BIN output file
grep ">" $MY_BIN_FILE | sed s/\>// > $MY_BIN_FILE.list.txt

module load samtools
#Grab the header from your bam file.  sam to bam fails if this doesnt exist
samtools view -H $MY_BAM_FILE > $MY_INTERMEDIATE

#Cycle through each contig, grabbing all of the reads that map to it and write them to a new sam file
##without a header, we cant use uncompressed bam piping, and I dont want to grab the header multiple times in the loop.
for line in $(cat $MY_BIN_FILE.list.txt)
	do
	samtools view $MY_BAM_FILE $line >> $MY_INTERMEDIATE
	done
#Make sam a bam, sort it by name, and grab paired (-f 0x002), and single (-F 0x002) reads from the new sorted bam
samtools view -bS $MY_INTERMEDIATE -o $MY_INTERMEDIATE2
samtools sort -n $MY_INTERMEDIATE2 $MY_INTERMEDIATE2.sorted
samtools view -f 0x002 $MY_INTERMEDIATE2.sorted.bam | awk '{print "@"$1"\n"$10"\n+"$1"\n"$11}' | gzip > $MY_OUTPUT
samtools view -F 0x002 $MY_INTERMEDIATE2.sorted.bam | awk '{print "@"$1"\n"$10"\n+"$1"\n"$11}' | gzip > $MY_OUTPUT2 

#clean up after yourself
rm $MY_INTERMEDIATE
rm $MY_INTERMEDIATE2
rm $MY_INTERMEDIATE2.sorted.bam

#exit nicely because life is good
exit 0

