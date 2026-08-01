import sys, os

def bytes_to_int(byte1, byte2):
    return byte2*256 + byte1

if len(sys.argv) < 2:
    sys.exit("No filename provided")

filename = sys.argv[1]

if not os.path.isfile(filename):
    raise FileNotFoundError(f"Filename {filename} is invalid")
    exit(1)

with open(filename) as file:
    code = [0]*4 + [int(v, 16) for v in file.read().split()]

if len(code) > 65532:
    raise ValueError("File is too large")

code += [0] * (65536 - len(code))

if any(v < 0 or v > 255 for v in code):
    raise ValueError("Byte value outside 0x00 to 0xFF")


code[0], pc = 4, 4

while True:
    pc = bytes_to_int(code[0], code[1])
    source = bytes_to_int(code[pc], code[pc+1])
    dest = bytes_to_int(code[pc+2], code[pc+3])

    next_pc = (pc + 4) & 0xFFFF
    next_pc_lo = next_pc & 0xFF
    next_pc_hi = next_pc >> 8

    if pc > 65532: break

    if source == 2:
        user_input = input()
        source_value = ord(user_input[0]) if user_input else 0
    else:
        source_value = code[source]
    
    if dest == 0:
        next_pc_lo = source_value
    elif dest == 1:
        next_pc_hi = source_value
    elif dest == 2:
        print(chr(source_value), end="")
    elif dest == 3:
        print()
        exit(source_value)
    else:
        code[dest] = source_value

    code[0] = next_pc_lo
    code[1] = next_pc_hi
