def power(x,n):
    multi = 0
    if n == 0:
        multi = 1
    else:
        for i in range (n):
            if multi == 0:
                multi += x
            else:
                multi = multi*x
    return multi
 
print(power(5,3))