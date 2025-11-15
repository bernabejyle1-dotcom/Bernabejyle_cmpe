amount = 0
balance = 1000
pin_number = 2621

def Welcome_message():
    print("Welcome to my bank")
    print("----------------")
    print("please enter your card")


def card_reader(isCardInserted):
    if isCardInserted == "YES":
        print("Card is inserted")
        return True
    else:
        return False

def input_and_validate_pin_number(inputPinNumber):
    for i in range(3):
        if i == 4:
            print("Card is Blocked. please contact your bank")
            return False

        inputPinNumber = input("Please input your PIN Number")
        if inputPinNumber == pin_number:
            return True

        else:
            print("wrong Pin Number. Please try again")

def transaction_selection():
    transaction = input("Please select your transaction")
    return transaction

def transaction_validation(amount, balance):
    if balance > amount:
        return True
    else:
        print("Insufficient balance. Card will reject")
        return False

def card_ejection():
    print("card is ejected. Please get your card")

def cash_dispensing():
    print("Cash is being dispensed... Please take your money.")

def print_receipt(amount):
    global balance
    balance = balance
    print("Remaining balance : " + str(balance))
    print("please get your receipt")

while True:
    Welcome_message()
    isCardInserted = input("Is card inserted?")

    if not card_reader(isCardInserted):
        continue

    print("Next Steps")
    input_and_validate_pin_number("")
    print("Next steps")

    transaction = transaction_selection()

    if transaction.lower() == "withdraw":
        amount = int(input("Please enter your amount: "))
        if transaction_validation(amount, balance):
            print("Withdraw operation started...")
            time.sleep(2)
            card_ejection()
            cash_dispensing()
            time.sleep(2)

            balance -= amount

            print(f"Remaining balance : {balance}")
            time.sleep(1)
            print_receipt(amount)
        else:
            card_ejection()
            continue


    elif transaction.lower() == "check balance":
        print("Check Balance Operation Started...")

    else:
        card_ejection()
        continue





