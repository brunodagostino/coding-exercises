def removeStars(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if s[i] != "*":
            stack.append(s[i])
        else:
            if len(stack) > 0:
                stack.pop()
        
    return "".join(stack)


# Test cases
test_cases = [
    "leet**cod*e",
    "erase*****",
    "**e**rase***"
]

for s in test_cases:
    result = removeStars(s=s)
    print(result)