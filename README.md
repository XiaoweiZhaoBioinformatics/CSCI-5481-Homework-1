# CSCI-5481-Homework-1
 Analysis of SARS-CoV-2 DNA sequences

# Background
The purpose of this exercise is to get you familiar with downloading and processing genomic data, and with thinking about the differences between coding sequencing and non-coding sequences and differences between nucleotide (DNA) and amino acid (protein) sequences.

# Steps
1. Download the whole-genome and separate-gene DNA sequences of SARS-CoV-2, the virus that causes COVID-19. Two sequence files were used here: `SARS-CoV-2_whole_genome.fna` and `SARS-CoV-2_separate_genes.fna`.

2. Write a program that counts how many times each 3-character codon (substring of 3 characters) appears in the whole-genome file, starting with characters 1-3, then characters 4-6, and so on till the end of the genome. If there are extra characters at the end because it is not perfectly divisible by 3, just ignore the last one or two. The output files are comma-separated (CSV) files with the codon string in column 1 and the total count in column 2.

3. Run the program on both input DNA files: the whole-genome file, and the file with the genome split into separate genes. 

The program runs like this:

```sh	
python count_codons.py input.fna output.csv
```

The results are saved in `SARS-CoV-2_whole_genome_output.csv` and `SARS-CoV-2_separate_genes_output.csv`.

4. Write a program that makes a barplot comparing side-by-side the counts of each codon in the two different files, sorted by count in the separate-gene file.

The program runs like this:


```sh
python make_barplot_codon.py SARS-CoV-2_whole_genome_output.csv SARS-CoV-2_separate_genes_output.csv
```

The results are as follows:

![codon_barplot.pdf](https://github.com/user-attachments/files/18220880/codon_barplot.pdf)

5. Write a program that converts the codon counts from the above two CSV files to amino acid counts using the genetic code. Then make a similar barplot comparing amino acid counts between the two files.

The program runs like this:


```sh
python make_barplot_aa.py SARS-CoV-2_whole_genome_output.csv SARS-CoV-2_separate_genes_output.csv
```

The results are as follows:

![amino_acid_barplot.pdf](https://github.com/user-attachments/files/18220886/amino_acid_barplot.pdf)

6. Where is the largest discrepancy in amino acid counts between the coding sequences and the whole genome sequence, and why?

> The largest discrepancy in amino acid counts between the whole genome sequence and the coding sequences is due to stop codons. In the file containing only coding sequences, there are 12 stop codons, each corresponding to one of the 12 coding gene sequences. In contrast, the whole genome sequence contains 774 stop codons, which is significantly more than those found in the coding sequences.

> The main reason for this discrepancy lies in differences in reading frames. For the whole genome sequence, translation could start at any nucleotide (1st nucleotide in this case), leading to random frame shifts. This allows many sequences to be misinterpreted as stop codons, even in non-coding regions. However, in coding sequences, each sequence begins with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA), following a pattern of start codon–protein-coding region–stop codon. Because the reading frame is fixed in coding sequences, stop codons only appear once in each coding sequence. The slight difference in how frames are formed has a huge impact on the codon counts across the genome. 

> In the whole genome, many regions are non-coding, and the identification of stop codons within these regions does not have meaningful biological information. Only the coding regions of the genome are transcribed and translated into functional proteins. 
