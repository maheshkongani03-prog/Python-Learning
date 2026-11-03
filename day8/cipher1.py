import string
original_list=list(string.ascii_lowercase)
print(original_list)
def ceasar(original_text,shift_amount,dir):
    encrypted_word=""   
    if dir=="decode":
        shift_amount*=-1
    for letter in original_text:
        index=original_list.index(letter)+shift_amount
        index%=len(original_list)
        encrypted_word+=original_list[index]
    print(f"The {dir}d message is:{encrypted_word}")
to_continiue=True
while to_continiue:
    direction=input("Type 'encode' to encrypt ,type 'decode' to decrypt:\n").lower()
    text=input("type your message:\n").lower()
    shift_num=int(input("Type the shift number:\n"))
    ceasar(text,shift_num,direction)
    again=input("Enter y/n to do it again\n").lower()
    if again=='n':
        to_continiue=False
        print("Nice to Meet You")



        
