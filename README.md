# COPYCAT

# Intro

COPYCAT is a OISC esolang.
It uses a virtual computer with little-endian von Neumann architecture, 4 reserved addresses and a 16-bit address space. (`0x0000` to `0xFFFF`)

The only instruction you have is a COPY (hence the name): copy the value stored in one address to another address, overwriting it. For example, to copy the value stored in address `0x1234` to address `0x5678`: `34 12 78 56`
Because it is a OISC, specifying the opcode isn’t supported because it’s not needed.
Additionally, COPYCAT code is allowed to modify itself.

# Reserved Addresses and Memory Mapping

- `0x0000` - The low byte of the address of the current instruction, AKA the PC. This can be freely read and written.
- `0x0001` - The high byte of the address of the current instruction, AKA the PC. This can be freely read and written.
- `0x0002` - The I/O byte. Reading this will instead use the ASCII value of a single byte taken from stdin, while writing to this will output the character with the ASCII value corresponding to the byte value written, to stdout.
- `0x0003` - The halt byte. Writing to this will immediately halt execution of the program with the byte value written being used as the exit code.

**The code is stored in memory** starts at address `0x0004`.
Additionally, all reserved addresses other than the program counter remain `0x00`, even when written to.
# Example Programs

## Truth Machine

```copycat
02 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 04
00 04 02 00
FF FF 03 00
FF

00 00 FF FF
04 00 02 00
FF FF 00 00
```

## Cat

```copycat
00 00 FF FD
FF FF 03 FF
02 00 FE FF
FE FF 02 00
FE FF 0B 00
FF FD 00 00
```
