import re

# print(input_string)
def find_coord_after_first_parens(index, input):
    # returns index after closing parens
    counter = 0
    for i in range(index, len(input)):
        if input[i] == '(':
            counter += 1
        if input[i] == ')':
            counter -= 1
        if counter == 0:
            return i + 1
        
def latex_to_text(input_string):

    # Define the regular expression pattern to match the character you want to replace
    pattern = r'\t'

    # Define the replacement character
    replacement = r'\\t'

    # Use the re.sub() function to replace all occurrences of the character in the string
    
    input_string = re.sub(r"\\\\", ".", input_string)
    input_string = re.sub(r"\\end{array} \\", "", input_string)
    input_string = re.sub(r"\\begin{array}{c}", "", input_string)
    input_string = re.sub("left", "", input_string)
    input_string = re.sub("right", "", input_string)
    input_string = re.sub("cdot", "*", input_string)
    input_string = re.sub("neg", "(-1)*", input_string)
    input_string = re.sub(r'\t', r'\\t', input_string)
    input_string = re.sub(r'\f', r'\\f', input_string)
    input_string = re.sub('{', '(', input_string)
    input_string = re.sub('}', ')', input_string)
    input_string = re.sub(r'\\to', '->', input_string)
    input_string = re.sub(r'\rightarrow', '->', input_string)
    input_string = input_string[1:]
    if input_string[0] == '(' and input_string[-1] == ')':
        input_string = input_string[1:-1]


    # input_string = '(' + input_string + ')'

    while "frac" in  input_string:
        index = input_string.index("frac") + 4
        div_pos = find_coord_after_first_parens(index, input_string)
        input_string = input_string[:div_pos] + '/' + input_string[div_pos:]
        input_string = input_string.replace("frac", "", 1)

    input_string = input_string.replace('\\', "")
    return input_string

if __name__ == "__main__":
    # input_string = "\lim_{a\to\frac{2}{5}}\frac{3a-2\sin{\pi}a}{3a^{3}-5}"
    # input_string = "\\( \\begin{array}{c}x=5 \\\\ x^{2}+7 x+6 \\\\ y^{\\sin x}+\\cosh ^{2} x\\end{array} \\)"
    input_string =  "\(3 + 3 =\)"
    input_string = " \( \lim _{n \rightarrow \infty} \frac{1}{n}= \)"
    text = latex_to_text(input_string)

    print(text)
