# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def run_length_encoding(s):
    o = []
    for i in s:
        if o and o[-1] == i:
            o[-2] = o[-2] + 1
        else:
            o.append(1)
            o.append(i)
    return ''.join(map(str, o))


def run_length_decoding(s):
    o = ""
    i = 0
    while i < len(s):
        j = int(s[i])
        while j > 0:
            o += s[i+1]
            j -= 1
        i += 2
    return o


if __name__ == "__main__":
    s = "aaaabbbccdaa"
    print "input string:", s
    print "encoded string:", run_length_encoding(s)
    print "decoded string:", run_length_decoding(run_length_encoding(s))