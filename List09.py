def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a=0
    x=[]
    while True:
        if fruits[a]=='apple':
            x.append(a)
        a+=1
        if a==5:
            break
    x.insert(0,len(x))
    return x