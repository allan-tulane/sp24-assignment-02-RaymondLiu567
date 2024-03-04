"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
  # Convert BinaryNumber objects to integer values
  x_val = x.decimal_val
  y_val = y.decimal_val

  # Base case for recursion
  if x_val < 10 or y_val < 10:  # can be adjusted to a higher base case for efficiency
      return BinaryNumber(x_val * y_val)

  # Calculate the size of the numbers.
  n = max(len(x.binary_vec), len(y.binary_vec))
  m = n // 2

  # Split x and y into two halves
  xL, xR = split_number(x.binary_vec)
  yL, yR = split_number(y.binary_vec)

  # Recursive calls for the three products
  z0 = subquadratic_multiply(xR, yR)
  z2 = subquadratic_multiply(xL, yL)

  # Compute (xL + xR)(yL + yR)
  sum_xL_xR = binary2int(list(map(lambda a, b: str(int(a) + int(b)), xL.binary_vec, xR.binary_vec)))
  sum_yL_yR = binary2int(list(map(lambda a, b: str(int(a) + int(b)), yL.binary_vec, yR.binary_vec)))
  z1 = subquadratic_multiply(sum_xL_xR, sum_yL_yR)

  # Subtract z2 and z0 from the product (xL + xR)(yL + yR)
  z1 = BinaryNumber(z1.decimal_val - z2.decimal_val - z0.decimal_val)

  # Final computation
  return BinaryNumber((z2.decimal_val << (2 * m)) + (z1.decimal_val << m) + z0.decimal_val)

def time_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  result = f(BinaryNumber(x), BinaryNumber(y))
  end = time.time()
  return (end - start) * 1000, result


    
    

