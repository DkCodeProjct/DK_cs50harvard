def main():
    dollars = dollarsToFloat(input("mealCose:_ "))
    tipPrecnt = precntagToFloat(input("tipPrecentage:_ "))
    tip = dollars * tipPrecnt
    print(f"Leave:{tip:.2f}")

def dollarsToFloat(dllr):
    rm_dollor = dllr.replace("$","")
    return float(rm_dollor)

def precntagToFloat(prcnt):
    rm_prectag = prcnt.replace("%","")
    precntgConvert = float(rm_prectag) / 100
    return precntgConvert

if __name__ == "__main__":
    main()

