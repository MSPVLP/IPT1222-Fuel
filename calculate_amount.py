

def calculate_amount(qty, tax, rate):
    """
    this function calculates the gross amount, tax amount, net amount
    :param qty:float
    :param tax:float
    :param rate:float
    :return:List - gross amount, tax amount, net amount
    """

    gross_amount = round(qty * rate, 2)
    tax_amount = round(rate * tax/100, 2)
    net_amount = round(gross_amount-tax_amount, 2)
    return [gross_amount, tax_amount, net_amount]


def test_calculate_amount():
    print(calculate_amount(2.0, 12.2, 105.5))
    print(calculate_amount(3, 10, 200))


if __name__ == "__main__":

    test_calculate_amount()

