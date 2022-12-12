

def get_vehicle_number():
    """
    This function get the vehicle number from user
    return:It produces the veh_no
    """
    veh_no = input("Enter Your Vehicle Number:")
    return veh_no


if __name__ == "__main__":
    vno = get_vehicle_number()
    print("Your Vehicle Number is:", vno)
