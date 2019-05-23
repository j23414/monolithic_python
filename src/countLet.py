#! /usr/bin/env python3
# Auth: Jennifer Chang
# Date: 2019/05/23

from typing import List


def count_let(seq_str: str) -> List[str]:
    count_result = {}
    for c in seq_str:
        if c in count_result:
            count_result[c] = count_result[c] + 1
        else:
            count_result[c] = 1
    # Sort dictionary
    count_result = sorted(count_result.items(), key=lambda t: t[0])
    return count_result


def main():
    seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print(seq)
    print(count_let(seq))


if __name__ == "__main__":
    main()
