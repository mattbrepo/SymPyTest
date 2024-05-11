# SymPyTest
Test of [SymPy](https://docs.sympy.org/) package.

**Language: Python**

**Start: 2024**

## Why
I wanted to try [SymPy](https://docs.sympy.org/) which is a Python package for symbolic mathematics. 

## A few tests
Check the equality of two expressions:

$$ \ln(1 + \exp(a) + \exp(b) + \exp(c) + 1) = \ln(\exp(b - a) + \exp(c - a) + \frac{1}{\exp(a)} + 1) + a $$

```python
expr1 = sp.log(sp.exp(a) + sp.exp(b) + sp.exp(c) + 1)
expr2 = sp.log(sp.exp(b - a) + sp.exp(c - a) + 1/sp.exp(a) + 1) + a
print(sp.simplify(expr1-expr2) == 0)

True
```

Numeric evaluation:
```
expr1_num = expr1.subs({a: 700, b: 600, c: 10})
expr1_num.evalf()

700.0
```

Unit conversion:
```
expr_u = (5 * spu.cm + 3 * spu.m).simplify()
spu.convert_to(expr_u, spu.m).n()

3.05m
```

## Partial derivatives
I wrote a code to calculate the partial derivatives for all the variables of a function. This code can be helpful to determine the gradient of a function.

Example, given the function:

$$ f = \left(- l + \sqrt{\left(x_{1} - x_{2}\right)^{2} + \left(y_{1} - y_{2}\right)^{2} + \left(z_{1} - z_{2}\right)^{2}}\right)^{2} $$

where _l_ is a constant and _x1, x2, y1, y2, z1, z2_ are the variables, the corresponding gradient is:

$$ \nabla f = \left[ \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \frac{\partial f}{\partial y_1}, \frac{\partial f}{\partial y_2}, \frac{\partial f}{\partial z_1}, \frac{\partial f}{\partial z_2} \right] $$

and the first of the 6 partial derivatives (_x1_) is:

$$ \frac{\partial f}{\partial x_1} = \frac{2 \left(- l + \sqrt{\left(x_{1} - x_{2}\right)^{2} + \left(y_{1} - y_{2}\right)^{2} + \left(z_{1} - z_{2}\right)^{2}}\right) \left(x_{1} - x_{2}\right)}{\sqrt{\left(x_{1} - x_{2}\right)^{2} + \left(y_{1} - y_{2}\right)^{2} + \left(z_{1} - z_{2}\right)^{2}}} $$

## Resources
A [playlist](https://www.youtube.com/playlist?list=PLSE7WKf_qqo1T5VV1nqXTj2iNiSpFk72T) of introductory videos.