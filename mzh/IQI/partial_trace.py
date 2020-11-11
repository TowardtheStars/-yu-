from sympy import *
import itertools
from pysnooper import snoop
from sympy.parsing.latex import parse_latex

def dagger(M):
	return transpose(conjugate(M))


def partial_trace(M, dim, base=2):
    
    if M.shape[0] == M.shape[1] and log(M.shape[0], base) % 1 == 0:
        mat_dim = log(M.shape[0], base)
        if isinstance(dim, int):
            dim = (dim,)
        re_dim = mat_dim - len(dim)
        
        dim = [mat_dim - d - 1 for d in dim]
        dim = sorted(dim, reverse=True)
        R = zeros(base ** re_dim)

        
        def get_index(num):
            for d in dim:
                num = num // (base ** (d+1)) * (base ** (d)) + num % (base ** d)
            return num
        
        indexes = [ (i, j)
            for (i, j) in itertools.product(range(base ** mat_dim), repeat=2)
                    if all([i & int(base ** d) == j & int(base ** d) for d in dim])
        ]
        
        for (i, j) in indexes:
            idx = i * (base ** mat_dim) + j
            
            r_idx = get_index(i) * (base ** re_dim) + get_index(j)
            R[get_index(i), get_index(j)] += M[i, j]
        return simplify(R)
            
    else:
        raise IndexError

def from_string(expr, state_symbols=('0', '1')):
        import re
        regexp_ket = re.compile('\|[' + ''.join(state_symbols) +']*>')
        base_kets = regexp_ket.findall(expr)
        state_dict = {}
        size = len(base_kets[0]) - 2
        
        def get_idx(state_):
            return int(state_[1:-1], base=2)

        def unitary_col(idx, size):
            re = zeros(2 ** size, 1)
            re[idx] = 1
            return re

        for base_ket in base_kets:
            idx = get_idx(base_ket)
            expr = expr.replace(base_ket, 'state_' + str(idx))
            state_dict['state_' + str(idx)] = unitary_col(idx, size)
        state_dict['dagger'] = dagger
        re_mat = parse_expr(expr,state_dict)
        return simplify(re_mat)



psi = from_string('sqrt(7)/4*(|000>+|010>)+1/4*(|101>-|111>)')
rho = psi * dagger(psi)
rho_A = partial_trace(rho, 0)
rho_B = partial_trace(rho, 1)
rho_C = partial_trace(rho, 2)

print(rho_A.eigenvals())
print(rho_B.eigenvals())
print(rho_C.eigenvals())


phi_p = from_string('(|00> + |11>)/sqrt(2)')
rho_p = simplify(3 * phi_p * dagger(phi_p) / 4 + Identity(4).as_explicit()/16)
print(latex(rho_p))
print(rho_p.eigenvals())
