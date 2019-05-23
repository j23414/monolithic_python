#! /usr/bin/env python3
# Auth: Jennifer Chang
# Date: 2019/05/23


def dna2rna(seq: str) -> str:
    rna = seq.replace("T", "U").replace("t", "u")
    return rna


def main():
    seq = "GATGGAACTTGACTACGTAAATT"
    print(seq)
    print(dna2rna(seq))


if __name__ == "__main__":
    main()
