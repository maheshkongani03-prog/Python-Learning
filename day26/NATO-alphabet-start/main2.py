import pandas 



data=pandas.read_csv("nato_phonetic_alphabet.csv")
studemt_daf=pandas.DataFrame(data)
phonetic={row.letter:row.code for  (index,row) in data.iterrows()}
#print(phonetic)

user_input=input("Enter your name:").upper()
output=[phonetic[letter] for letter in user_input]
print(output)