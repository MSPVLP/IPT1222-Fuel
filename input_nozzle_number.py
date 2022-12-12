MAX_Nozzle_Number = 12


def input_nozzle_number():
    """
    It gets the nozzle number the user
    :return: nozzle number
    """
    inp = input("Enter the nozzle number:")
    try:
        value = int(inp)
    except ValueError:
        return None
    return value


def validate_nozzle_number(nozzle_number):
    """It validates the nozzle number.
         If it is valid, return true."""

    if MAX_Nozzle_Number >= nozzle_number > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    num = input_nozzle_number()
    if num is None:
        print("You entered wrong value.")
    else:
        print(num)
    val = validate_nozzle_number(num)
    if val:
        print("The number is valid")
    else:
        print("The number is invalid")













