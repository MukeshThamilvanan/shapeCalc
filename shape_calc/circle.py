

def area_circle(radius):
    print("To find the area of a circle!")
    radius = float(input("Enter the radius: "))
    area_eq_cir = pi * (radius ** 2)
    print("The area of the circle is " + str(area_eq_cir))
area_circle(1)

def peri_circle(radius):
    print("To find the circumference of the Circle!")
    radius = float(input("Enter the radius: "))
    peri_eq_cir = 2 * pi * radius
    print("The circumference of the circle is " + str(peri_eq_cir))

peri_circle(2)