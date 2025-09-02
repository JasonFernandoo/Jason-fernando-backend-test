# fungsi d(n)
def d(n):
    return n + sum(int(digit) for digit in str(n))

# fungsi generate 1 sampai 5000
def generate_all_numbers(limit):
    generatedNumbers = set ()
    for i in range(1, limit + 1):
        generatedNumbers.add(d(i))
    return generatedNumbers

# fungsi cari self number
def self_numbers(limit):
    generated_numbers = generate_all_numbers(limit)
    selfNumbers = [i for i in range(1, limit + 1) if i not in generated_numbers]
    return selfNumbers

# fungsi sum self numbers
def sum_self_numbers(limit):
    return sum(self_numbers(limit))

limit = 5000
total_self_numbers = sum_self_numbers(limit)
print("Jumlah semua self-numbers dari 1 sampai 5000 =", total_self_numbers)