# %%
import sympy as sp
from sympy.solvers.inequalities import reduce_inequalities
from sympy.functions.elementary import piecewise
from sympy.matrices import eye
import sympy.physics.units as spu
import numpy as np

# %%
# --- equality test
a = sp.Symbol('a', real=True)
b = sp.Symbol('b', real=True)
c = sp.Symbol('c', real=True)

expr1 = sp.log(sp.exp(a) + sp.exp(b) + sp.exp(c) + 1)
expr1

# %%
expr2 = sp.log(sp.exp(b - a) + sp.exp(c - a) + 1/sp.exp(a) + 1) + a
expr2

# %%
print(f'are they the same: {sp.simplify(expr1-expr2) == 0}')

# %% just a test
expr2_diff = expr2.diff(a)
expr2_diff = expr2_diff.simplify()
expr2_diff

# %%
sp.limit(expr2_diff, a, 700)

# %% --- limit test
a = sp.Symbol('a', real=True)
b = sp.Symbol('b', real=True)

expr1_mod = sp.log(sp.exp(a) + sp.exp(b) + 1)
expr1_mod

# %% numeric substituition
expr1_num = expr1.subs({a: 700, b: 600, c: 10})
expr1_num

# %%
expr1_num.evalf()

# %% lambdify
expr1_np = sp.lambdify([a, b], expr1_mod)
a_points = np.linspace(-100, 100, 1000)
rndx = np.random.rand(1000)
b_points = np.array([rnd * a + a for a, rnd in zip(a_points, rndx)])
expr1_np(a_points, b_points)

# %% limit
sp.limit(expr1, a, 700, '+-')

# %% identity matrix
A = eye(5)
A

# %% units
expr_u = (5 * spu.cm + 3 * spu.m).simplify()
expr_u

# %% 
spu.convert_to(expr_u, spu.m).n()