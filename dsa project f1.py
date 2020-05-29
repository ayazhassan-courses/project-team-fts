function



    



def binary_converter(num):
    result=""

    if num>1:
        binary_converter(num//2) 
    result+= str(n%2)
    return result


def string_to_binary(txt):
    l= [ord(items) for items in txt]
    result=""
    for i in l:
        result+=binary_converter(i)


    return result


    


