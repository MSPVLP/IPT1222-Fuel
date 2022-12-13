
def input_product_code():
    """
    It gets product code from user
    :return pro_code:str - product code
    """
    pro_code = input("Enter the product code:")
    return pro_code


def validate_product_code(pro_code: str):      # example of type annotation
    if(pro_code[0].isalpha()) and (pro_code[1:3].isdigit()) and len(pro_code) == 3:
        return True

    else:
        return False


def sanitize_product_code(pro_code: str):
    return pro_code.upper()


def test_validate_product_code():
    assert validate_product_code("P01") == True
    assert validate_product_code("p01") == True
    assert validate_product_code("P1P") == False
    assert validate_product_code("p00") == True
    assert validate_product_code("p10") == True
    assert validate_product_code("P  ") == False
    assert validate_product_code("   ") == False
    assert validate_product_code("_p01") == False
    assert validate_product_code("@p01")== False
    assert  validate_product_code("#P1p")==False
    assert validate_product_code("&p0p") == False
    print("All tests passed.")


def test_sanitize_product_code():
    assert validate_product_code(sanitize_product_code("P01")) == True
    print("All tests passed.")


if __name__ == "__main__":
    test_validate_product_code()
    test_sanitize_product_code()
