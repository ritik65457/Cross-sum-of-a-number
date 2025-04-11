def cross_sum(number):
    return sum(int(digit) for digit in str(abs(number)))

# Example usage
num = int(input("Enter a number: "))
result = cross_sum(num)
print(f"Cross sum of {num} is: {result}")
