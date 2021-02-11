words = ["pro", "gram", "merit", "program", "it", "programmer"]
patterns = "program"
matching = [s for s in words if patterns in s]


def check(n):
    array =  ['pro', 'gram', 'merit', 'program', 'it', 'programmer']
    result = ''
    cut = False
    for i in array:
        if i in n:
            result += '{}, '.format(i)
        else:
            cut = True
    if cut:
        pass
    else:
        print(result)


check('programmerit')

print(matching)