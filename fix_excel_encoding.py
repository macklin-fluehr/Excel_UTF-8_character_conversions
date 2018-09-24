

""" Use this file to process excel files that have messed up encoding """

import weird_excel_character_dictionary as w
import unidecode

weird_chars = w.dic

in_file = 'MASTER.csv'
out_file = 'Clean_MASTER.csv'


# Read in the file
with open(in_file, 'r') as file :
  filedata = file.read()

# Replace the target string
for char in list(weird_chars.keys()):
    filedata = filedata.replace(char, weird_chars[char])

filedata = unidecode.unidecode(filedata)

# Write the file out again
with open(out_file, 'w') as file:
  file.write(filedata)
