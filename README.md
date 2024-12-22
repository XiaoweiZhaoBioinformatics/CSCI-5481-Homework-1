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

[codon_barplot.pdf](https://github.com/user-attachments/files/18220874/codon_barplot.pdf)


