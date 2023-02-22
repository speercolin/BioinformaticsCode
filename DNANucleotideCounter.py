import string

# Example DNA sequence.
dna_sequence = "ACGTAGCATGACTAGGCAACTATCAG"

# Nucleotide counting method which only allows strings for input.
def count_nucleotides(string):
    # Initialize nucleotide count.
    count_a = 0
    count_t = 0
    count_c = 0
    count_g = 0

    # Iterate through the string counting each nucleotide.
    for nucleotide in string:
        if nucleotide == 'A':
            count_a += 1
        elif nucleotide == 'T':
            count_t += 1
        elif nucleotide == 'C':
            count_c += 1
        elif nucleotide == 'G':
            count_g += 1

    # Print the amount of each nucleotide counted + percentage.
    print("Amount of A's: ", count_a)
    print("Amount of T's: ", count_t)
    print("Amount of C's: ", count_c)
    print("Amount of G's: ", count_g)

# Calling the method.
count_nucleotides(dna_sequence)
