# Given a string of round, curly, and square open and closing
# brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


def main(str):
    map = {")":"(",
           "]":"[",
           "}":"{"}
    stack = []
    entry = ("(", "{", "[")
    res = (")", "}", "[")
    if str == "":
        return True
    if str[0] in res:
        return False
    for i in str:
        if i in entry:
            stack.append(i)
        else:
            v = stack.pop()
            if v != map[i]:
                return False
    return stack == []


if __name__ == "__main__":
    s1 = "([])[]({})"
    s2 = "([)]"
    s3 = "((()"
    print main(s1)
    print main(s2)
    print main(s3)
