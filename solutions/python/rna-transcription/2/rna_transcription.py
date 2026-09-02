"""
Transcribe a DNA strand into its RNA complement.
"""
def to_rna(dna_strand):
    """
    Transcribe a DNA strand into its RNA complement.

    :param dna_strand: The DNA sequence to transcribe.
    :return: The corresponding RNA complement.
    """
    rna_check = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_strand = ""
    # if dna_strand == "":
    #     return rna_strand

    for rna in dna_strand:
        rna_strand += rna_check[rna]
        
    return rna_strand
