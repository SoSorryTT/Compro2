# Make this code DRY

def num_digits(a):
    a_digits = 0
    while a > 0:
        a = a // 10
        a_digits = a_digits + 1
    return a_digits

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits."""

    return num_digits(a) == num_digits(b)

print(same_length(50, 70))
print(same_length(50, 100))
print(same_length(10000, 12345))
