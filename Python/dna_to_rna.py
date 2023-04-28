import string

# Method that converts Thymine into Uracil.
def convert_to_mRNA(string):
    converted_dna = string.replace('T', 'U')
    print("DNA sequence successfully converted into mRNA. ")
    print(converted_dna)
