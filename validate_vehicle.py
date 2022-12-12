

def validate_vehicle_number(vno):
    """ This function validate the vehicle number

    :param vno: vehicle number -string
    :return: vehicle number -string

    """
    if(vno[0:2].isalpha()) and (vno[2:6].isalnum()) and (vno[-4:].isdigit()):
            return True
    else:
           return False


if __name__ == "__main__" :
    res = validate_vehicle_number("TML5758")

    if res:
        print("The vehicle number is valid")
    else:
        print("The vehicle number is not valid")

