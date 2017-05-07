def stringsConstruction(A, B):
    b = list(B)
    count = 0
    num_str_iter = 0
    for i in range(len(B) // len(A)):
       count = 0
       for i in A:
           if i in b:
               b.remove(i)
               count += 1
               if count == len(A):
                   count = 0
                   num_str_iter += 1

    return num_str_iter