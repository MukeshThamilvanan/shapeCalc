
def area_triangle(base, height):
    print("To find the area of a Triangle!")
    base = float(input("Enter a base: "))
    height = float(input("Enter a height: "))
    area_eq_tri = .5 * base * height
    print("The area of the Triangle is " + str(area_eq_tri))

area_triangle(1,2)

def peri_triangle(side1, side2, side3):
    print("To find the perimeter of a Triangle!")
    side1 = float(input("Enter a side: "))
    side2 = float(input("Enter another side: "))
    side3 = float(input("Enter the last side: "))
    peri_eq_tri = side1 + side2 + side3
    print("The perimeter of the Triangle is " + str(peri_eq_tri))

peri_triangle(3,4,5)