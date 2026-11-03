def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculation():
    n1=float(input("Enter the first number:"))
    should_continue=True
    while should_continue:
        for symbols in operators:
            print(symbols)
        operation=input("Enter the Operation:")
        n2=float(input("Enter the Next Number:"))
        answer=operators[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {answer}")
        to_cont=input("do you want to continue? 'y' for yes. 'n' for otherwise:")
        if to_cont=='y':
            n1=answer
        elif to_cont=='n':
            should_continue=False
            print("\n"*20)
            calculation()
            
        else:
            print("plaease type correct key 'y' to continue, 'n' to stop:")
            n1=answer
calculation()
