# program to demonstrate proper usage of try / except


def input_demo():
    inp = input("Enter integer value:")
    try:
        val = int(inp)
    except ValueError:
        val = None
    return val


def input_demo2():
    inp = input("Enter integer value:")
    try:
        val = int(inp)
    except ValueError:
        return None
    return val


def input_demo3():
    try:
        inp = input("Enter float value:")
        val = float(inp)
    except (ValueError, EOFError):
        return None
    return val


if __name__ == "__main__":
    x = input_demo3()
    if x is None:
        print("You entered wrong value.")
    else:
        print(x)