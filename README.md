# Memory Weeknesses

---

## Vulnerability Exploitation in Linux Program

### Description

This exercise involves a compiled Linux program (`out1.ex`), its source code (`c1.ex`), and its compilation script (`sh1.ex`). Your task is to identify a vulnerability in the program, leverage root permissions (preferably through suid), and exploit the program to write your ID card information to a file located at `txt.id/`.

**Important Notes:**
1. Assume ASLR is disabled.
2. Provide any assembly code assisting your solution in separate text files with detailed documentation.
3. Your solution may be probabilistic. If it doesn't work consistently, explain under which circumstances it may fail and propose improvements.

### Files

1. **ex1.out** - Compiled Linux program.
2. **ex1.c** - Source code of the program.
3. **ex1.sh** - Compilation script.

### Instructions

1. Grant root permissions to the program (recommended using suid) to enable the execution of the `setuid` command.
2. Find and exploit a vulnerability in the program to make it write your ID card information to a file at `txt.id/`.

---

## Vulnerability Exploitation in Windows Program

### Description

This exercise involves a compiled Windows program (`exe.rop`) designed for the Windows operating system. Your objective is to make the program print your ID card information to the screen.

### Files

1. **exe.rop** - Compiled Windows program.

### Instructions

1. Identify a vulnerability in the Windows program (`exe.rop`).
2. Exploit the vulnerability to make the program print your ID card information to the screen.
