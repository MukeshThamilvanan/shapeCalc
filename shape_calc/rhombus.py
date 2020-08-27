def perimeter_rh(side):
    print("To find the perimeter of a rhombus!")
    side = float(input("Enter a side: "))
    peri_eq_rh = side * 4
    print("The perimeter of a rhombus is " + str(peri_eq_rh))

perimeter_rh(1)

def area_of_rhombus(side):
    print("To find the area of a rhombus!")
    dia1 = float(input("Enter a diagonal: "))
    dia2 = float(input("Enter an another diagonal: "))
    area_rh = ((dia1 * dia2) / 2)
    print("Area of rhombus:" + str(area_rh))

area_of_rhombus(3)

def diagon_length_rh(area):
    print("To find the diagonal length of a rhombus!")
    area = float(input("Enter the area: "))
    dia_len_eq_rh = pow(area, 1/2)
    print("The diagonal length of a rhombus is " + str(dia_len_eq_rh))
diagon_length_rh(1)