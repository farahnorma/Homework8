"""
Lab 9-2 Module: exceptions.py

Define read_float_gt0() so it throws exception if float <=0.0 is read,
    otherwise return the float

"""

def read_float_gt0():
    in_value = float(input("Enter a float > 0.0: "))
    if in_value>0.0:
        return in_value

    raise Exception #user entered a bad value <= 0.0

    # read a float:
    # if > 0.0, return it
    # else throw a new Exception exception
    # if user enters an invalid float, what exception is thrown?

def main():
    while True:
        try:
            returned = read_float_gt0()
            break
        except ValueError:
            print("Not a float. Please re-enter.")
            continue
        except Exception:
            print("Negative or Zero value. Please re-enter.")
            continue
        # if we get here, no problems so exit loop via break
        # finish the exception handlers below...


        # except < put name of exception for bad floats here >:
        #   print("bad float")
        # except Exception:
        #   print("Exception occurred.")
        #   print("float must be > 0.0.  Please reenter.")

    print(returned)

main()
