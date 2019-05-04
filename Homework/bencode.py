import itertools as it
import re
import string

def encode(val):
    if isinstance(val, int):
        return b'i' + str(val).encode() + b"e"
    elif isinstance(val, bytes):
        return  str(len(val)).encode() + b":" + val
    elif isinstance(val, str):
        return  encode(val.encode("ascii"))
    elif isinstance(val, list):
        return  b"l" + b"".join(map(encode, val)) + b"e"
    elif isinstance(val,dict):
        if all(isinstance(val, bytes) for i in val.keys()):
            items = list(val.items)
            items.sort
            return b"d" + b"".join(map(encode, it.chain(*items))) + b"e"
        else:
            raise ValueError("No keys")
    raise ValueError("you must enter  only :int, bytes, list ,dict; not %s", type(val) )
 


def decode(val):
    if val.startswith(b"i"):
        equally = re.match(b"i(-?\\d+)e", val)
        return int(equally.group(1)), val[equally.span()[1]:]
    elif val.startswith(b"l") or val.startswith(b"d"):
        l = []
        end = val[1:]
        while not end.startswith(b"e"):
            elem, end = decode(end)
            l.append(elem) 
        end = end[1:]
        if val.startswith(b"l"):
            return l, end
        else:
            return {i: j for i, j in zip(l[::2], l[::2])} , end
    elif any(val.startswith(i.encode()) for i in string.digits):
        m = re.match(b"(\\d+):", val)
        lenght = int(m.group(1))
        end_i = m.span()[1]
        start = end_i
        last_end = end_i + lenght
        return val[start:last_end] , val[last_end:]
    else:
        raise ValueError("incorrect input")
        

    if isinstance(val, str):
        val = val.encode("ascii")
    ret,end = decode(val)
    if end:
        raise ValueError("icorrect input")
    return ret

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
