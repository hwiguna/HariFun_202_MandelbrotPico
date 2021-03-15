MAX_ITER = 80

def mandelbrot(c):
    z,n = 0,0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n