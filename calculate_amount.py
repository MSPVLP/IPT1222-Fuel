

def calculate_amount(qty, tax, rate):
    """

    :param qty:
    :param tax:
    :param rate:
    :return:
    """
    amount = qty * rate + (rate * tax / 100)
    total_amount = round(amount, 2)
    return total_amount


if __name__ == "__main__":

    total = calculate_amount(2, 12, 100)
    print(total)