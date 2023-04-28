#!/bin/bash

# Setting the motif sequence value
motif="ACTG"

# Stores the DNA sequence from the inputted Fasta file
seq=$(grep -v '>' sequence.fasta | tr -d '\n')

# Counting the number of occurrences of the motif and storing the value
motif_count=$(echo $seq | grep -o $motif | wc -l)

# Outputting the results
echo "The motif $motif has been found $motif_count in the DNA sequence."
