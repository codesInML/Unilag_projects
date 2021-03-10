# implementing the lagrange's formular

def lagrange(x_val, x_arr, y_arr):
    total = 0
    
    for i in range(len(x_arr)):
        numerator_count = 1
        denominator_count = 1
        for j in x_arr:
            if (j != x_arr[i]):
                numerator_count *= x_val - j
                denominator_count *= x_arr[i] - j
        total += (numerator_count * y_arr[i])/denominator_count
    return f'The value of f({x_val}) = {total}'

# lagrange(9, [5, 7, 11, 13, 17], [150, 392, 1452, 2366, 5202])
print(lagrange(656, [654, 658, 659, 661], [2.8156, 2.8182, 2.8189, 2.8202]))
print(lagrange(15, [4,5,7,10,11,13], [48,100,294,900,1210,2028]))