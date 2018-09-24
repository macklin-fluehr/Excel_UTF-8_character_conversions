# Excel_UTF-8_character_conversions

## Fix Excel Encoding

This is a simple script to repair a csv. It replaces the junky excel characters with UTF-8 characters.

For best results, to ensure that excel doesn't mess up again in the future, this module also uses
the unidecode library to transform the UTF-8 characters into closely approximated ASCII. 

## Weird_excel_character_dictionary

The dictionary of junky excel stuff. This is not an inclusive dictionary, but it contains many of
the characters you are most likely to come across. Feel free to add to it.
