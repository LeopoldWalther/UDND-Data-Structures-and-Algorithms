# O(log(n))

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        print('Input has to be of type integer.')
        return None

    elif number < 0:
        return -1

    elif number == 0 or number == 1:
        return number

    else:
        start = 1
        end = number

        while start <= end:
            mid = end - start // 2
            squared_mid = mid ** 2

            if squared_mid == number:
                return mid

            elif squared_mid < number:
                start = mid + 1
                guess = mid

            else:
                end = mid - 1

        return guess


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
