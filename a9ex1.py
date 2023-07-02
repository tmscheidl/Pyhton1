"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 1
"""

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", type=str, required=True, help="Specifies the path of the input file from which patterns should be extracted.")
parser.add_argument("-p", "--patterns", nargs="+", type=str, required=True, help="Specifies a non-empty list of string patterns that are regular expressions.")
parser.add_argument("-s", "--separator", type=str , default="\n", help="The string to use for separating extracted pattern matches.")
parser.add_argument("-e", "--encoding", type=str , default="utf-8", help="The character encoding to use for accessing all files (input reading and output writing).")

args = parser.parse_args()

p_input_file = args.input_file
p_pattern_list = args.patterns
p_sep = args.separator
p_encod = args.encoding

files_count = 0


with open(p_input_file, "r", encoding=p_encod) as f:
    content = f.read()

    for p_pattern in p_pattern_list:
        list_of_matches = []

        for i, m in enumerate(re.finditer(p_pattern, content)):
            list_of_matches.append(m.group())

        new_file_wp = f'{p_input_file}_{files_count}.txt'

        with open(new_file_wp, "w", encoding=p_encod) as nf:
            nf.write(f"regex: {p_pattern}\n")
            nf.write(p_sep.join(list_of_matches))
            files_count += 1