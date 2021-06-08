import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1:
nato_alphabet = {row.letter: row.code for index, row in alphabet_df.iterrows()}
# print(nato_alphabet)

# TODO 2:
word = input("Enter a word: ").upper()
output_list = [nato_alphabet[char] for char in word]
print(output_list)
