def create_map() -> dict[str, str]:
    map = dict()

    map["{"] = "}"
    map["["] = "]"
    map["("] = ")"

    return map

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def peek(self) -> str:
        return self.stack[-1]
    
    def push(self, data) -> None:
        self.stack.append(data)
    
    def pop(self) -> str:
        return self.stack.pop()

def is_balanced(s) -> str:
    result = "YES"
    stack = Stack()
    map = create_map()

    for c in s:
        if (c == "{") or (c == "[") or (c == "("):
            stack.push(data=c)
        else:
            if stack.is_empty():
                result = "NO"
                break

            if map[stack.pop()] != c:
                result = "NO"
                break
    
    return result


# Test cases
test_cases = [
    "()",
    "[]",
    "{}",
    "(())",
    "[]]",
    "{}}",
    "({[()]})",
    "({[]})",
    "({[)}])",
    "({[(])})",
    "({[(])}{[]})",
    "{[()]}",
    "{[(])}",
    "{{[[(())]]}}",
]

for brackets_string in test_cases:
    balanced = is_balanced(s=brackets_string)
    print(balanced)