

def area_of_rectangle(length, width):
    print("To find the area of a rectangle!")
    length = input("Enter a length: ")
    width = input("Enter a width: ")
    area_rec = float(length) * float(width)
    print("Area of a rectangle is Length times Width.")
    print("Area of rectangle:" + str(area_rec))
area_of_rectangle(1, 2)

def diagon_length_rc(length, width):
    print("To find the diagonal length of a rectangle!")
    length = float(input("Enter a length: "))
    width = float(input("Enter a width: "))
    dia_len_eq = ((width ** 2) + (length ** 2))
    print("The diagonal length of a square is " + str(dia_len_eq))

diagon_length_rc(3, 4)

def perimeter_rc(length, width):
    print("To find the perimeter of a rectangle!")
    length = float(input("Enter a length: "))
    width = float(input("Enter a width: "))
    peri_eq_rc = 2 * (length + width)
    print("The perimeter of a rectangle is " + str(peri_eq_rc))

perimeter_rc(5, 6)

