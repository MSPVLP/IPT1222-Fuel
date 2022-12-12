

def validate_vehicle_number(vno):
    """ This function validate the vehicle number

    :param vno: vehicle number -string
    :return: vehicle number -string

    """
    vl = len(vno)
    if vl == 10:
        if(vno[0:2].isalpha()) and (vno[2:6].isalnum()) and (vno[6:vl-1].isdigit()):
            return True
        else:
            return False
    else:
      return False


if __name__ == "__main__" :
    res = validate_vehicle_number("TN76AI9767")

    if res:
        print("The vehicle number is valid")
    else:
        print("The vehicle number is not valid")

