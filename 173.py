# Write a function to flatten a nested dictionary. Namespace the keys with a period.
# For example, given the following dictionary:
# {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
# it should become:
# {"key": 3, "foo.a": 5, "foo.bar.baz": 8}


def flattened(inp, parent, out):
    if len(inp) <= 0:
        return
    for k in inp:
        if parent == "":
            new_key = k
        else:
            new_key = parent + "." + k
        v = inp[k]
        if isinstance(v, dict) and len(v) > 0:
            flattened(v, new_key, out)
        else:
            out[new_key] = v
    return out


if __name__ == "__main__":
    inp_json = {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
    print flattened(inp_json, "", {})