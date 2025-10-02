# [program name]
# [your name]
# [date]
# AS Computer Science

# [comment]
def depositMoney(totalBalance):
    try:
        status = True

        while (status == True):
            enterAmount = float(input("Enter deposit(£): "))
            totalBalance = totalBalance + enterAmount
            print(f"Your total balance is: {totalBalance}")
        return totalBalance
        
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def one():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        totalBalance = 0
        totalBalance = depositMoney(totalBalance)
        
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
