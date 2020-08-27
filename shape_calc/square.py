

def area_of_square(side):
    print("To find the area of a square!")
    side = input("Enter a side: ")
    area_sq = float(side) * float(side)
    print("Area of a square is side times itself.")
    print("Area of Square:" + str(area_sq))

area_of_square(3)


def diagon_length_sq(side):
    print("To find the diagonal length of a square!")
    side = float(input("Enter a side: "))
    dia_len_eq = pow(2, 1/2) * side
    print("The diagonal length of a square is " + str(dia_len_eq))
diagon_length_sq(1)

def cccircle_area(side2):
    print("To find the circumcircle of a square!")
    side2 = input("Enter a side: ")
    dia_len_eq_sq = pow(2, 1/2) * float(side2)
    cccirle_eq_sq = 3.14 * (dia_len_eq_sq / 2)
    print("The circumcircle of a sq is " + str(cccirle_eq_sq))

cccircle_area(2)

def perimeter_sq(side3):
    print("To find the perimeter of a square!")
    side2 = input("Enter a side: ")
    peri_eq_sq = side3 * 4
    print("The perimeter of a square is " + str(peri_eq_sq))

perimeter_sq(3)

