def reverseWords(s: str) -> str:
    result = ""
    s = s.strip()

    i = 0
    flag = False
    word = ""
    while i < len(s):
        if s[i] != " ":
            word += s[i]
            flag = False

            if i == len(s) - 1:
                result = word + result

        if s[i] == " " and flag == False:
            result = s[i] + word + result
            word = ""
            flag = True

        i += 1

    return result


# Test cases
test_cases = [
    "the sky is blue",
    "  hello world  ",
    "a good   example"
]

for s in test_cases:
    result = reverseWords(s)
    print(result)
