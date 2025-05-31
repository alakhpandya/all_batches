def median(*args):
    l1 = list(args)
    l1.sort()

    if len(l1) % 2 != 0:
        return l1[int((len(l1)+1)/2)]
    else:
        return (l1[int(len(l1)/2)] + l1[int(len(l1)/2)+1])/2