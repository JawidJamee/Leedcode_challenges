def fizzBuzz(n):
    """
    do not for get "self" if you want to test with leedcode compiler
    :type n: int
    :rtype: List[str]
    """

    mylist = []
    for i in range(1, n + 1):
        dev_by_3 = (i % 3 == 0)
        dev_by_5 = (i % 5 == 0) 
        if dev_by_3 and dev_by_5:
            s = 'FizzBuzz'
        elif dev_by_3:
            s = 'Fizz'
        elif dev_by_5:
            s = 'Buzz'
        else:
            s = str(i)
        mylist.append(s)
    return mylist


print(fizzBuzz(15))