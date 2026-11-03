def calculator():   
    n1=int(input("What is the First Number:"))
    print("+\n-\n*\n/\n")
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    operation={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
    }
    to_continue='y'
    Previous_result=0
    choice=input("choose the opeeration:")
    n2=int(input("Enter the next number:"))
    Previous_result+=operation[choice](n1,n2)
    print(f"{n1} {choice} {n2} = {Previous_result}")
    should_continue=True
    while should_continue:
        to_continue=input("want to continue? y/n:").lower()
        if to_continue=='y':
            print("+\n-\n*\n/\n")
            choice=input("choose the opeeration:")
            n2=int(input("choose the next number:"))
            Final_Previous_result=operation[choice](Previous_result,n2)
            print(f"{Previous_result} {choice} {n2}  = {Final_Previous_result}")
            Previous_result=Final_Previous_result
        elif to_continue=='n':
            should_continue=False
            print("\n"*20)
            calculator()
            
        else:
            print("plaease type correct key 'y' to continue, 'n' to stop:")
            Previous_result=Final_Previous_result
calculator()
