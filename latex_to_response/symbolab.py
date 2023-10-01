import sympy as sp
from sympy.parsing.latex import parse_latex
import re
# Run This in your terminal in addition to installing the modules above: <pip install antlr4-python3-runtime==4.11>

escape_char_map = {8:'\\b', 7:'\\a', 12:'\\f', 10:'\\n', 13:'\\r', 9:'\\t', 11:'\\v'}

def escape_string_to_reg_string(s):
    reg_string =  ''.join( [ escape_char_map.get( ord(c), c ) for c in s ] )
    reg_string = re.sub(r'{{', '{', reg_string)
    reg_string = re.sub(r'}}', '}', reg_string)
    return reg_string


def latex_to_result(latex_input):
    latex_no_escape = escape_string_to_reg_string(latex_input)
    print("Latex Expression:", latex_no_escape)
    sympy_expression = parse_latex(latex_no_escape)
    print("SymPy Expression:", sympy_expression)
    result = sympy_expression.doit()
    print("Result:", result)
    return result

if __name__ == "__main__":
    latex = 'x -'
    # latex = "\lim_{a\to\frac{2}{5}}\frac{3a-2\sin{\pi}a}{3a^{3}-5}"
    # latex = "\lim_{{x \to \infty}} \frac{1}{x}"
    result = latex_to_result(latex)
