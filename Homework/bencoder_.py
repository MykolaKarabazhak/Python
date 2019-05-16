from collections import abc, OrderedDict
from functools import singledispatch 


D,L,I,E,C = b'dlie:'

def _encode_seq(val, ba, type_): # d , l
    ba.append(type_)
    for i in val:
        encode_any(i , ba)
    ba.append(E)

def _flattern(d):
    for k ,v in d:
        yield k
        yield v


@singledispatch
def encode_any(val,ba):
    raise NotImplementedError


@encode_any.register(int)
def encode_int(val, ba):
    ba.append(I)
    ba.extend(str(val).encode())
    ba.append(E)

@encode_any.register(OrderedDict)
def encode_o_dict(val, ba):
    _encode_seq(_flattern(val.items()), ba , D)


@encode_any.register(abc.Mapping)
def encode_dict(val,ba):
    _encode_seq(_flattern(sorted(val.items())), ba , D)

@encode_any.register(abc.Sequence)
def encode_list(val,ba):
    _encode_seq(val ,ba, L)  

@encode_any.register(str)
def encode_str(val,ba):
    encode_any(val.encode(), ba)


@encode_any.register(bytes)
def encode_bites(val,ba):
    ba.extend(str(len(val)).encode())
    ba.append(C)
    ba.extend(val)

def decode_int(bs, i, stop=E):
    d = bs.index(stop)
    res = bs[i:d].decode()
    return int(res), d + 1

def decode_bytes(bs, i):
    blen, i = decode_int(bs, i, stop=C)
    j = i + blen
    return bs[i:j], j

def _decode_seq(bs, i):
    out = []    
    while True:
        v ,i = decode_any(bs, i)
        if v == None:
            return out, i
        else:
            out.append(v)
    return out
        
def decode_list(bs, i):
    return _decode_seq(bs, i)

def decode_dict(bs, i):
    seq, i = decode_any(bs, i)
    return OrderedDict(zip(*[iter(seq)] * 2))


DECODE_DICT = {
    D:decode_dict,
    L:decode_list,
    I:decode_int,
    E:lambda _, i:(None, i+1)
}




def decode_any(bs, i):
    b = bs[i]
    if b in DECODE_DICT:
        return DECODE_DICT[b](bs, i+1) 
    else:
        return decode_bytes(bs , i)
def decode(bs):
    result = decode_any(bs , 0)
    return result

def encode(val):
    ba = bytearray()
    encode_any(val, ba)
    return bytes(ba)



|
