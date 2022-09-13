import string

normal = string.ascii_uppercase
normal = [*normal]
reverse = normal[::-1] 

input = "SOMEPLAIN TEXT"
output = []
for i in input:
    output.append(reverse[normal.index(i)])
    
print(''.join(output))

input = []
for i in output:
    input.append(normal[reverse.index(i)])
    
print(''.join(input))