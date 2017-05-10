def mathPractice(numbers):
    return reduce(lambda y,(i,x): y+x if i%2!=0 else y*x ,enumerate(numbers), 1)
