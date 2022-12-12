

def sanitize_vehicle_number(vehicle_number: str):
    """
    :param vehicle_number: str - It receives a vehicle number
    :return: str - It returns the trimmed vehicle number
    """
    trimmed_veh_no = vehicle_number.strip()
    return trimmed_veh_no.upper()


if __name__ == "--main--" :
    veh_no = sanitize_vehicle_number("      tn76as2345 ")
    print("After sanitize vehicle number:", veh_no)















