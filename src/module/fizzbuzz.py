# python3.7.5
def fizzbuzz(target_num: int) -> str:
    if target_num % 3 == 0 and target_num % 5 == 0:
        msg = 'fizzbuzz'
    elif target_num % 3 == 0:
        msg = 'fizz'
    elif target_num % 5 == 0:
        msg = 'buzz'
    else:
        msg = str(target_num)

    return msg
