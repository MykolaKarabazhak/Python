
""" попытка решения код не работает  я пришел пожже к решинию но до сдачи работы не успел доделать """

number = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelf"
}

opertion ={
    "+":"add",
    "/":"division",
    "=":"equel",
    "*":"multiply"
}


rank = {
     3:"hudert",
     4:"thousend",
     7:"milion",
}

sufiks = {
    1:"teen",
    2:"ty",
}
def check_str(func):
    def wrapper(enter):
        if isinstance(enter, str):
            try:
                func(enter)
            except TypeError:
                print("You must enter only number and '*,-,\,+',=")
        else:
           print(" this string  is not valid ")
    return wrapper

def number_str(numb):
    some_string = ""
    a = len(numb)
    if a in rank:
        some_string += rank[a]
    for i in (numb):
        some_string += i
def oper_sring(i):
    pass
@check_str
def parser_(enter):
    string_math = ""
    numb = ""
    for i in enter:
        if i in number.keys():
            numb += i
        elif i in opertion.keys():
            number_str(numb)
            numb = ""
            string_math += " " +  opertion[i]
        else:
            raise TypeError
    print(string_math)
enter = "215*"
parser_(enter)
