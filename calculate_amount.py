

def calculate_amount(qty, tax, rate):
    """
    this function calculates the gross amount, tax amount, net amount
    :param qty:float
    :param tax:float
    :param rate:float
    :return tuple - gross amount, tax amount, net amount
    """

    gross_amount = round(qty * rate, 2)
    tax_amount = round(rate * tax/100, 2)
    net_amount = gross_amount - tax_amount
    amounts = (gross_amount, tax_amount, net_amount)
    return amounts


def test_calculate_amount():
    print(calculate_amount(2.0, 12.2, 105.5))
    print(calculate_amount(3, 10, 200))


if __name__ == "__main__":

    test_calculate_amount()

