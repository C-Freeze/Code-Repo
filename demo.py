import lib_func

def main():
    x = 10
    y = 5
    print(f"{x} + {y} = {lib_func.add(x, y)}")
    print(f"{x} - {y} = {lib_func.subtract(x, y)}")
    print(f"{x} * {y} = {lib_func.mul(x, y)}") #TODO: Add this
    print(f"{x} / {y} = {lib_func.div(x, y)}") #TODO: Add this
    
if __name__ == "__main__":
    main()