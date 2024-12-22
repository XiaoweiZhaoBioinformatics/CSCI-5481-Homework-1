import csv
import sys
import os

def count_codons(seq_file):
    
    # Open input sequence file
    input_file = open(seq_file,"rt")

    line = ''
    sequence = ''
    
    for n in input_file:
    
        # Read each line in input_file
        line = n.rstrip()
    
        # If this line is starting with ">", this line is header, then continue; else, save that line in sequence 
        if line.startswith(">"):
            continue
        else:
            sequence += line
    
    # Close file that has opened
    input_file.close()
    
    # Count how many codons are there in the sequence
    seq_len = len(sequence)
    num_codon = seq_len//3

    # Identify each codon and their counts
    count_table = {}

    for i in range(num_codon):
        seq = sequence[i*3:i*3+3]
        if seq not in count_table:
            count_table[seq] = 1
        else:
            count_table[seq] += 1
    
    return count_table

def main():
    
    if len(sys.argv) != 2:
        print("Usage: count_codons.py <seq_file>")
        sys.exit(1)
        
    inputfile = sys.argv[1]
    results = count_codons(inputfile)

    # Generate output file name
    base_name = os.path.basename(inputfile)
    name_without_extension = os.path.splitext(base_name)[0]
    outputfile_name = f"count_table_{name_without_extension}.csv"

    # The following codes that write a dictionary to a csv file is derived from ChatGPT

    # Open the file in write mode
    with open(outputfile_name, 'w', newline='') as output_file:
        
        # Create a writer object with comma as the delimiter
        writer = csv.writer(output_file)
        
        # Write each key-value pair as a row in the csv file
        for key, value in results.items():
            writer.writerow([key, value])

    # Close file that has opened
    output_file.close()

if __name__ == "__main__":
    main()
