# Write and test a function that takes an integer as its parameter and returns the factors of that integer. (A factor is an integer which can be multiplied by another to yield the original).
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Test the function
num_to_factorize = 24
result_factors = find_factors(num_to_factorize)

print(f"The factors of {num_to_factorize} are: {result_factors}")