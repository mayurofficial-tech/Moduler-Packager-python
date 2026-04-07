import math


def calculate_factorial(n):
    if n == 0 or n==1:
        return 1

    return n*calculate_factorial(n-1)


def solve_compound_interest():
    principal=int(input("Enter the principal: "))
    rate=float(input("Enter the rate(in %): "))
    time=int(input("Enter the time(in years): "))
    compounding_frequency=int(input("Enter the compounding frequency(per year): "))
    amount=principal*(1+rate/compounding_frequency)**(time*compounding_frequency)
    return amount

def trigonometric_calculations():
    angle_degrees=int(input("Enter the angle in degrees: "))
    import math
    angle_radians = math.radians(angle_degrees)
    sin_value=math.sin(angle_radians)
    cos_value=math.cos(angle_radians)
    tan_value=math.tan(angle_radians)
    return sin_value, cos_value, tan_value

def area_of_geometry_shapes(shape,*dimensions):
    if shape=="circle":
        redius=dimensions[0]
        return math.pi *(redius**2)
    elif shape=="rectangle":
        length,width=dimensions
        return length*width
    elif shape=="triangle":
        base,height=dimensions
        return 0.5*base*height
    else:
        return "shape not recognized"

def main():
    while True:
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometry Shapes")
        print("5. Back to Main Menu")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print("=" * 30)
            n = int(input("Enter the number of factors: "))
            calculate_factorial(n)
            print("=" * 30)
        elif ch == 2:
            print("=" * 30)
            solve_compound_interest()
            print("=" * 30)
        elif ch == 3:
            print("=" * 30)
            trigonometric_calculations()
            print("=" * 30)
        elif ch == 4:
            print("=" * 30)
            shapes = input("Enter the shapes(circle, rectangle, triangle): ")
            if shapes == "circle":
                print("=" * 30)
                redius = int(input("Enter the radius of circle: "))
                print("Area of circle=", area_of_geometry_shapes(shapes, redius))
                print("=" * 30)
            elif shapes == "rectangle":
                print("=" * 30)
                length = float(input("Enter the length of rectangle: "))
                width = float(input("Enter the width of rectangle: "))
                print("Area of rectangle=", area_of_geometry_shapes(shapes, length, width))
                print("=" * 30)
            elif shapes == "triangle":
                print("=" * 30)
                base = float(input("Enter the base of triangle: "))
                height = float(input("Enter the height of triangle: "))
                print("Area of triangle=", area_of_geometry_shapes(shapes, base, height))
                print("=" * 30)
            else:
                print("=" * 30)
                print("shape not recognized")
                print("=" * 30)
            print("=" * 30)
        elif ch == 5:
            break
        else:
            print("=" * 30)
            print("Invalid input")
            print("=" * 30)

if __name__ == "__main__":
    main()
