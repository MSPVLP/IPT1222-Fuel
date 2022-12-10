

def validate_something(thing:str):      # example of type annotation
    if thing.find("TN") >= 0 or thing.upper() == "VIP" or len(thing)==10:
        return True
    else:
        return False


def sanitize_something(thing:str):
    return thing.upper()


def test_validate_something():
    assert validate_something("TN") == True
    assert validate_something("I am from TN") == True
    assert validate_something("VIP") == True
    assert validate_something("Vip") == True
    assert validate_something("nobody") == False
    assert validate_something("James Bond from T.N.") == False
    assert validate_something("iamtenchar") == True
    assert validate_something("") == False
    print("All tests passed.")


def test_sanitize_something():
    assert validate_something(sanitize_something(" test input from tn ")) == True
    print("All tests passed.")


if __name__ == "__main__":
    test_validate_something()
    test_sanitize_something()

