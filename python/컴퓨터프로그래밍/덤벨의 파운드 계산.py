lbTokg = 0.453592
kgTolb = 2.204623
def round_five(int):
    intTOstr = str(int)
    return float(intTOstr[:7])

lb = int(input("파운드(lb)를 입력하세요 : "))
print(f"{lb} 파운드(lb)는 {round_five(lb * lbTokg)} 킬로그램(kg)입니다.")

kg = int(input("킬로그램(kg)를 입력하세요 : "))
print(f"{kg} 파운드(lb)는 {round_five(kg * kgTolb)} 킬로그램(kg)입니다.")

