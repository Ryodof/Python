def fibonnaci(number):
    if number<=1:
        return number
    return fibonnaci(number-1) + fibonnaci(number-2)

number = int(input())
print(fibonnaci(number))