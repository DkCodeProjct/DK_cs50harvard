def main():
    income = dollar_to_float(input("Enter_Income: $##.## : "))
    donate_precent = donate_to_flaot(input("Enter_Donate_Precentage: ##% : "))
    donation = income * donate_precent
    print(f"Total_Donation: ${donation:.2f}.")

def dollar_to_float(d_sign):
    ammount = float(d_sign[1:])
    return ammount

def donate_to_flaot(p_sign):
    precentage = float(p_sign[:-1]) / 100.0
    return precentage

if __name__ == "__main__":
    main()
