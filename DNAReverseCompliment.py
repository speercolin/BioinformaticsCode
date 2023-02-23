# Example DNA sequence.
dna_example = list("ACTAGAGCACGAGTTTACAGCT")

# Method that outputs the reverse compliment of the inputted DNA sequence.
def reverse_compliment(list):
    # Reversing DNA sequence & assigning to new variable.
    reversed_dna = list[::-1]

    # For loop which iterates through the DNA sequence, converting each nucleotide to it's complement.
    for i in range(len(reversed_dna)):
        if reversed_dna[i] == 'A':
            reversed_dna[i] = 'T'
        elif reversed_dna[i] == 'T':
            reversed_dna[i] = 'A'
        elif reversed_dna[i] == 'C':
            reversed_dna[i] = 'G'
        elif reversed_dna[i] == 'G':
            reversed_dna[i] = 'C'

    # Converts the reverse compliment list into a string.
    compliment_string = "".join(reversed_dna)

    # Prints the reverse complement of the original DNA sequence.
    print("Reverse compliment of original DNA sequence created: ")
    print(compliment_string)

# Test calling the method.
reverse_compliment(dna_example)
