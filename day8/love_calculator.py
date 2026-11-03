def calculate_love_score(name1,name2):
    name3=name1.lower()+name2.lower()
    print(name3)
    m1="true"
    m2="love"
    sum1=sum2=0
    for i in name3:
        if i in m1:
            sum1+=1
        if i in m2:
            sum2+=1
    sum=int(str(sum1)+str(sum2))

    print(sum)      
calculate_love_score("Angela Yu","Jack Bauer")
