import re
import functools
import sys

var = 'x'

def get_coefficient(t):
    coefficient_end_index = t.index('x')
    return int(t[:coefficient_end_index])


def get_degree(t):
    degree_start = t.index('^')
    return int(t[degree_start+1:])


def get_sign(t):
    return '+' if t[0] != '-' else '-'


def split_by_terms(p):
    p = p.replace("-", "+-")
    return list(filter(None,re.split('\\+', p))) # filter to remove empty strings in the list if there are any


def compare_degree(t1, t2):
    return get_degree(t2) - get_degree(t1)


def filter_zero_coefficients(p):
    return not (get_coefficient(p) == 0)


def sort_by_term_degree(p, add_helpers=True):
    splt = split_by_terms(p)
    if add_helpers:
        splt = add_helper_symbols(splt)
    return sorted(splt, key=functools.cmp_to_key(compare_degree))


def add_helper_symbols(poly_list):
    for i, term in enumerate(poly_list):
       if var not in poly_list[i]:
           poly_list[i] += (var + '^0')
       elif var in poly_list[i] and '^' not in poly_list[i]:
           poly_list[i] += '^1'

       negative = poly_list[i][0] == '-'
       if negative and poly_list[i][1] == var:
           poly_list[i] = '-1' + poly_list[i][1:]
       elif not negative and poly_list[i][0] == var:
           poly_list[i] = '1' + poly_list[i]

    return poly_list

def remove_helper_symbols(p):
    without_zeros = []
    for t in p:
        if get_coefficient(t) != 0:
            without_zeros.append(t)

    return "+".join(without_zeros).replace("+-", "-")\
                                 .replace(var+"^1", var)\
                                 .replace(var+"^0", "")\
                                 .replace("1"+var, var)


def balance_polynomials(p1,p2):
    missing_term_default_value = "0x^" + str(-sys.maxsize)
    c=0
    while not(get_degree(p1[0]) == get_degree(p2[0]) and get_degree(p1[-1]) == get_degree(p2[-1]) and len(p1) == len(p2)):
        p1c = p1[c] if c < len(p1) else missing_term_default_value
        p2c = p2[c] if c < len(p2) else missing_term_default_value
        if get_degree(p1c) > get_degree(p2c):
            val = '0' + var + '^' + str(get_degree(p1c))
            p2.append(val) if c > len(p2) else p2.insert(c, val)
        elif get_degree(p1c) < get_degree(p2c):
            val = '0' + var + '^' + str(get_degree(p2c))
            p1.append(val) if c > len(p1) else p1.insert(c, val)
        else:
            c+=1

    return p1,p2

def subtract_polynomials(p1, p2):
    p1,p2 = balance_polynomials(p1,p2)
    ret = []
    for i in range(len(p1)):
        diff = str(get_coefficient(p1[i]) - get_coefficient(p2[i])) + var + '^' + str(get_degree(p1[i]))
        ret.append(diff)
    return ret


def long_division(p1, p2): # divide p1 by p2
    print("Divide " + p1 + " by " + p2)
    p1 = sort_by_term_degree(p1)
    p2 = sort_by_term_degree(p2)

    quotient = []
    remainder = []

    while len(p1) != 0 and len(p2) != 0:
        first_non_zero_term=None
        for t in p1:
            if get_coefficient(t) != 0:
                first_non_zero_term = t
                break

        if get_degree(first_non_zero_term) < get_degree(p2[0]):
            remainder = p1
            break

        q_coefficient = int(get_coefficient(first_non_zero_term) / get_coefficient(p2[0]))
        q_degree = get_degree(first_non_zero_term) - get_degree(p2[0])
        q = str(q_coefficient) + var + '^' + str(q_degree)
        quotient.append(q)

        to_subtract = ""
        for i,t in enumerate(p2):
            sgn=""
            if i>0 and (get_sign(t)=='+' or (get_sign(t)=='-' and get_sign(q) == '-')):
                sgn='+'
            to_subtract += sgn + str(q_coefficient * get_coefficient(t)) + var + '^' + str(q_degree + get_degree(t))

        to_subtract = sort_by_term_degree(to_subtract, add_helpers=False)

        p1 = subtract_polynomials(p1, to_subtract)


    quotient = remove_helper_symbols(quotient)
    remainder = remove_helper_symbols(remainder)
    p2 = remove_helper_symbols(p2)

    return [quotient, [remainder, p2]]

r1 = long_division("x^4-3x^2+4x+5", "x^2-x+1")
print(r1)
r2 = long_division("x^3-3x^2+5x-3", "-2+x^2")
print(r2)