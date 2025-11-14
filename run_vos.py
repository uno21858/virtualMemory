from vm import VM, PAGE_SIZE

vm = VM()

addr = 3 * PAGE_SIZE + 10
print("Writing 99 to virtual address", addr)
vm.write_byte(addr, 99)

print("Reading back...")
value = vm.read_byte(addr)
print("Value =", value)

assert value == 99
print("✓ VM works!")

# Print final statistics
vm.print_stats()