with open("../Mail_Merge_Project_Start/Input/Names/invited_names.txt", "r") as f:
    names=f.readlines()
    

with open("../Mail_Merge_Project_Start/Input/Letters/starting_letter.txt","r") as letter:
    sss=letter.read()
    for i in range(len(names)):
        stripped_name=names[i].strip("\n")
        replaced_letter=sss.replace(f"[name]",stripped_name)
        with open(f"../Mail_Merge_Project_Start/Output/ReadyToSend/{stripped_name}.pdf", "w") as Final_Letter:
            Final_Letter.write(replaced_letter)
            