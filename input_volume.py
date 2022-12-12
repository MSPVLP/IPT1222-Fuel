

def input_volume():
    """It gets the input_volume from user """
    volume = input("How many liter to you want? ")
    try:
        val = int(volume)
    except ValueError:
        val = None
    return val


if __name__ == "__main__":
    vl = input_volume()
    if vl is None:
        print("Enter the volume properly")
        print("Incorrect")
    else:
        print(vl)






