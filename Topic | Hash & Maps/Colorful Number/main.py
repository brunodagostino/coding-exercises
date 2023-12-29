def is_colorful(n) -> bool:
    n = str(object=n)
    h = {}

    for i in range(len(n)):
        for j in range(i + 1, len(n) + 1):
            subseq = n[i:j]
            product = 1
            for digit in subseq:
                product *= int(digit)

            if subseq not in h:
                h[subseq] = product
            else:
                if h[subseq] == product:
                    return False

    return True


# Test cases
test_cases = [
    3245,
    326,
    12345,
]

for n in test_cases:
    result = is_colorful(n=n)
    print(result)