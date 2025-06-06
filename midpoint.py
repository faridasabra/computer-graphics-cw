def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0

    print("(", x + x_centre, ", ", 
               y + y_centre, ")", 
               sep = "", end = "") 
    
    if (r > 0) :
    
        print("(", x + x_centre, ", ",
                  -y + y_centre, ")", 
                  sep = "", end = "") 
        print("(", y + x_centre, ", ", 
                   x + y_centre, ")",
                   sep = "", end = "") 
        print("(", -y + x_centre, ", ", 
                    x + y_centre, ")", sep = "") 
    
    P = 1 - r 

    while x > y:
    
        y += 1

        if P <= 0: 
            P = P + 2 * y + 1
        else:         
            x -= 1
            P = P + 2 * y - 2 * x + 1
         
        if (x < y):
            break

        print("(", x + x_centre, ", ", y + y_centre,
                            ")", sep = "", end = "") 
        print("(", -x + x_centre, ", ", y + y_centre, 
                             ")", sep = "", end = "") 
        print("(", x + x_centre, ", ", -y + y_centre,
                             ")", sep = "", end = "") 
        print("(", -x + x_centre, ", ", -y + y_centre,
                                        ")", sep = "") 

        if x != y:
            print("(", y + x_centre, ", ", x + y_centre, 
                                ")", sep = "", end = "") 
            print("(", -y + x_centre, ", ", x + y_centre,
                                 ")", sep = "", end = "") 
            print("(", y + x_centre, ", ", -x + y_centre,
                                 ")", sep = "", end = "") 
            print("(", -y + x_centre, ", ", -x + y_centre, 
                                            ")", sep = "")
if __name__ == '__main__': 
    midPointCircleDraw(0, 0, 3)