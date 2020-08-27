
print("Welcome to Shape Calculator!")


def shape_calc():
    shapes = "(1)Square\n(2)Rectangle\n(3)Rhombus\n(4)Triangle\n(5)Circle\n(6)Quit \n"
    print("Choose a shape!")
    print(shapes)
    option = input("Choose a shape:")


    if option == "Square" or option == "1" or option == "square":
        print("You have chosen Square")
        sq_ops = "(1)Area \n(2)Diagonal Length \n(3)Circumcircle \n(4)Perimeter \n(5)Volume\n(6)Quit \n"
        print(sq_ops)
        sq_chos = input("For square, calculate: ")


        if sq_chos == "Area" or sq_chos == "1" or sq_chos == "area":
            print("To find the area of a square!")
            side = input("Enter a side: ")
            area_sq = float(side) * float(side)
            print("Area of a square is side times itself.")
            print("Area of Square:" + str(area_sq))
            shape_calc()


        elif sq_chos == "Diagonal Length" or sq_chos == "diagonal length" or sq_chos == "2":
            print("To find the diagonal length of a square!")
            side = float(input("Enter a side: "))
            dia_len_eq = pow(2, 1 / 2) * side
            print("The diagonal length of a square is " + str(dia_len_eq))
            shape_calc()


        elif sq_chos == "3" or sq_chos == "Circumcircle" or sq_chos == "circumcircle":
            print("To find the circumcircle of a square!")
            side2 = input("Enter a side: ")
            dia_len_eq_sq = pow(2, 1 / 2) * float(side2)
            cccirle_eq_sq = 3.14 * (dia_len_eq_sq / 2)
            print("The circumcircle of a square is " + str(cccirle_eq_sq))
            shape_calc()


        elif sq_chos == "4" or sq_chos == "Perimeter" or sq_chos == "perimeter":
            print("To find the perimeter of a square!")
            side3 = float(input("Enter a side: "))
            peri_eq_sq = (side3 + side3 + side3 + side3)
            print("The perimeter of a square is " + str(peri_eq_sq))
            shape_calc()

        elif sq_chos == "Volume" or sq_chos == "5" or sq_chos == "volume":
            print("To find the volume of a cube!")
            side4 = float(input("Enter a side: "))
            vol_cb = side4 * side4 * side4
            print("The volume of a cube is " + str(vol_cb))
            shape_calc()

        elif option == "quit" or option == "Quit" or option == "6":
            quit()

        else:
            print("Invalid option, choose from the given!")
            shape_calc()






    elif option == "Rectangle" or option == "2" or option == "rectangle":
        print("You have chosen Rectangle!")
        rc_ops = "(1)Area \n(2)Diagonal Length \n(3)Perimeter\n(4)Volume\n(5)Quit \n"
        print(rc_ops)
        rc_chos = input("For Rectangle, calculate: ")

        if rc_chos == "area" or rc_chos == "Area" or rc_chos == "1":
            print("To find the area of a rectangle!")
            length = input("Enter a length: ")
            width = input("Enter a width: ")
            area_rec = float(length) * float(width)
            print("Area of a rectangle is Length times Width.")
            print("Area of rectangle:" + str(area_rec))
            shape_calc()


        elif rc_chos == "Diagonal Length" or rc_chos == "diagonal length" or rc_chos == "2":
            print("To find the diagonal length of a rectangle!")
            length = float(input("Enter a length: "))
            width = float(input("Enter a width: "))
            dia_len_eq = ((width ** 2) + (length ** 2))
            print("The diagonal length of a rectangle is " + str(dia_len_eq))
            shape_calc()


        elif rc_chos == "Perimeter" or rc_chos == "perimeter" or rc_chos == "3":
            print("To find the perimeter of a rectangle!")
            length = float(input("Enter a length: "))
            width = float(input("Enter a width: "))
            peri_eq_rc = 2 * (length + width)
            print("The perimeter of a rectangle is " + str(peri_eq_rc))
            shape_calc()


        elif rc_chos == "Volume" or rc_chos == "4" or rc_chos == "volume":
            print("To find the volume of a cuboid!")
            height = float(input("Enter height: "))
            width = float(input("Enter width: "))
            lenght = float(input("Enter length: "))
            vol_cbd = height * width * lenght
            print("The volume of a cuboid is " + str(vol_cbd))
            shape_calc()

        elif option == "quit" or option == "Quit" or option == "5":
            quit()

        else:
            print("Invalid option, choose from the given!")
            shape_calc()





    elif option == "Rhombus" or option == "3" or option == "rhombus":
        print("You have chosen Rhombus!")
        rh_ops = "(1)Area \n(2)Diagonal Length \n(3)Perimeter\n(4)Quit \n"
        print(rh_ops)
        rh_chos = input("For Rhombus, calculate: ")

        if rh_chos == "area" or rh_chos == "Area" or rh_chos == "1":
            print("To find the area of a rhombus!")
            dia1 = float(input("Enter a diagonal: "))
            dia2 = float(input("Enter an another diagonal: "))
            area_rh = ((dia1 * dia2) / 2)
            print("Area of rhombus:" + str(area_rh))
            shape_calc()

        elif rh_chos == "Diagonal Length" or rh_chos == "diagonal length" or rh_chos == "2":
            print("To find the diagonal length of a rhombus!")
            area = float(input("Enter the area: "))
            dia_len_eq_rh = pow(area, 1 / 2)
            print("The diagonal length of a rhombus is " + str(dia_len_eq_rh))
            shape_calc()

        elif rh_chos == "Perimeter" or rh_chos == "perimeter" or rh_chos == "3":
            print("To find the perimeter of a rhombus!")
            side = float(input("Enter a side: "))
            peri_eq_rh = side * 4
            print("The perimeter of a rhombus is " + str(peri_eq_rh))
            shape_calc()

        elif option == "quit" or option == "Quit" or option == "4":
            quit()

        else:
            print("Invalid option, choose from the given!")
            shape_calc()




    elif option == "Triangle" or option == "4" or option == "triangle":
        print("You have chosen Triangle!")
        tr_ops = "(1)Area \n(2)Perimeter\n(3)Quit \n"
        print(tr_ops)
        tr_chos = input("For Triangle, calculate: ")

        if tr_chos == "area" or tr_chos == "Area" or tr_chos == "1":
            print("To find the area of a Triangle!")
            base = float(input("Enter a base: "))
            height = float(input("Enter a height: "))
            area_eq_tri = .5 * base * height
            print("The area of the Triangle is " + str(area_eq_tri))
            shape_calc()

        elif tr_chos == "perimeter" or tr_chos == "Perimeter" or tr_chos == "2":
            print("To find the perimeter of a Triangle!")
            side1 = float(input("Enter a side: "))
            side2 = float(input("Enter another side: "))
            side3 = float(input("Enter the last side: "))
            peri_eq_tri = side1 + side2 + side3
            print("The perimeter of the Triangle is " + str(peri_eq_tri))
            shape_calc()

        elif option == "quit" or option == "Quit" or option == "3":
            quit()

        else:
            print("Invalid option, choose from the given!")
            shape_calc()



    elif option == "circle" or option == "5" or option == "Cirlce":
        print("You have chosen Circle!")
        cr_ops = "(1)Area \n(2)Perimeter \n(3)Volume \n(4)Quit \n"
        print(cr_ops)
        cr_chos = input("For Circle, calculate: ")


        if cr_chos == "area" or cr_chos == "Area" or cr_chos == "1":
            print("To find the area of a circle!")
            radius = float(input("Enter the radius: "))
            area_eq_cir = 3.14 * (radius ** 2)
            print("The area of the circle is " + str(area_eq_cir))
            shape_calc()

        elif cr_chos == "perimeter" or cr_chos == "Perimeter" or cr_chos == "2":
            print("To find the circumference of the Circle!")
            radius = float(input("Enter the radius: "))
            peri_eq_cir = 2 * 3.14 * radius
            print("The circumference of the circle is " + str(peri_eq_cir))
            shape_calc()


        elif cr_chos == "volume" or cr_chos == "Volume" or cr_chos == "3":
            print("To find the volume of a sphere!")
            rad = float(input("Enter radius: "))
            vol_sp = (4/3) * 3.14 * (rad ** 3)
            print("The volume of a sphere is " + str(vol_sp))
            shape_calc()

        elif option == "quit" or option == "Quit" or option == "4":
            quit()

        else:
            print("Invalid text, choose from the given!")
            shape_calc()


    elif option == "quit" or option == "Quit" or option == "6":
        quit()



    else:
        print("Invalid option, choose from the given!")

        shape_calc()




if __name__ == "__main__":
    shape_calc()