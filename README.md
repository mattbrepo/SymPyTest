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

## Resources
A [playlist](https://www.youtube.com/playlist?list=PLSE7WKf_qqo1T5VV1nqXTj2iNiSpFk72T) of introductory videos.