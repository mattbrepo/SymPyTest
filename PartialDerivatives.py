# %%
import sympy as sp
from sympy.printing.latex import print_latex

def get_vars_expr1():
  x1, x2, y1, y2, z1, z2 = sp.symbols('x1 x2 y1 y2 z1 z2', real=True)
  my_vars = [x1, x2, y1, y2, z1, z2]
  l = sp.symbols('l', real=True) # costant
  f = (sp.sqrt(
    (x1 - x2)**2 +
    (y1 - y2)**2 +
    (z1 - z2)**2
  ) - l)**2
  return my_vars, f

def all_pd(my_vars, expr):
  for v in my_vars:
    print(f'Partial derivative of {v}')
    pd = sp.diff(expr, v)
    #print(pd)
    print_latex(pd)
    print(' ')

# %%
vars1, expr1 = get_vars_expr1()
print_latex(expr1)
expr1

# %%
print(f'Partial derivative of {vars1[0]}')
sp.diff(expr1, vars1[0]).evalf()

# %%
all_pd(vars1, expr1)

