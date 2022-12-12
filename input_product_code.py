
def input_product_code():
    """
    It get product code from user
    :return pro_code:
    """

    pro_code = input("Enter the product code:")
    return pro_code


def validate_product_code(pro_code: str):      # example of type annotation
    if pro_code.find("P01") >= 0 or pro_code.upper() == "p01" or len(pro_code) == 3:
        return True
    else:
        return False


def sanitize_product_code(pro_code: str):
    return pro_code.upper()


def test_validate_product_code():
    assert validate_product_code("P01") == True
    assert validate_product_code("p01") == True
    assert validate_product_code("P0") == True
    assert validate_product_code("P1") == True
    assert validate_product_code("p000") == False
    assert validate_product_code("p110") == False
    assert validate_product_code("P") == True
    assert validate_product_code("") == False
    print("All tests passed.")


def test_sanitize_product_code():
    assert validate_product_code(sanitize_product_code(" test input from P01 ")) == True
    print("All tests passed.")


if __name__ == "__main__":
    test_validate_product_code()
    test_sanitize_product_code()
