

def get_vehicle_number():
    """
    This function get the vehicle number from user
    return:It produces the veh_no
    """
    veh_no = input()
    return veh_no


if __name__ == "__main__":
    print("Enter Your Vehicle Number:")
    vno = get_vehicle_number()
    print("Your Vehicle Number is:", vno)
