#solve in Fewest steps 

def sorted_string(s):
    letters = ([c for c in s if c.isalpha()])
    digit =   ([c for c in s if c.isdigit()])
    return ''.join(letters + digit)

#Input Example
input_str = "B4A1D3"
output_str  = sorted_string(input_str)
print(output_str)