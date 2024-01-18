#Aiden Allison
#1/18/24
#M1Lab - Decision structures, loops and math
def calc_tax(income):
    flat = int(0)
    margin = int(0)
    if income > 0 and income <= 9875:
        margin = income * 0.10
        
    if income > 9876 and income <= 40125:
        flat = 986
        margin = (income-9875) * 0.12
        
    if income > 40125 and income <= 85525:
        flat = 4618
        margin = (income-40125) * 0.22
        
    if income > 85526 and income <= 163300:
        flat = 14606
        margin = (income-85525) * 0.24
        
    if income > 163301 and income <= 207350:
        flat = 47360
        margin = (income-163301) * 0.32
        
    if income > 207251 and income <= 518400:
        flat = 47368
        margin = (income-207350) * 0.35

    if income >= 518401:
        flat = 156325
        margin = (income-518400) * 0.37

        #caculate total tax
    return flat + margin

def main():
    run_again = ("yes")
    #get income
    while run_again == "yes":
        status = input("Please enter status (single,married,divorced.....): ")
        if status == ("single"):
                annualIncome = int(input("What is your annual income: "))
                total_tax = calc_tax(annualIncome)
                print(f"Your annual income is ${annualIncome:.2f} the total tax is ${total_tax:.2f}")
        else:
                print("The program only runs for single status")
                run_again = input("do you want to run again(yes or no): ") 
if __name__ == "__main__":
    main()
