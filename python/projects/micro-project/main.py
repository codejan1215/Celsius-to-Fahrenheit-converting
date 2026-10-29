def alu_simulator():
    print("--- 8-Bit ALU Simulator ---")
    instruction = input("Enter an 8-bit binary instruction (e.g., 10101100): ").strip()
    
    # 1. Input Validation
    if len(instruction) != 8 or not all(bit in '01' for bit in instruction):
        print("Error: Please enter exactly 8 binary digits (0s and 1s).")
        return

    # 2. Hardware Splitter Simulation (String Slicing)
    opcode_bin = instruction[0:2]   # First 2 bits
    operand1_bin = instruction[2:5] # Next 3 bits
    operand2_bin = instruction[5:8] # Final 3 bits

    # 3. Opcode Mapping
    operations = {
        "00": "AND",
        "01": "OR",
        "10": "XOR",
        "11": "ADD"
    }
    operation_name = operations.get(opcode_bin)

    # 4. Binary to Integer Conversion
    val1 = int(operand1_bin, 2)
    val2 = int(operand2_bin, 2)

    # 5. Logic Execution
    if operation_name == "AND":
        result = val1 & val2
    elif operation_name == "OR":
        result = val1 | val2
    elif operation_name == "XOR":
        result = val1 ^ val2
    elif operation_name == "ADD":
        result = val1 + val2

    # 6. Execution Output
    print("\n--- Execution Step-by-Step ---")
    print(f"Instruction : {instruction}")
    print(f"Opcode      : {opcode_bin} -> {operation_name}")
    print(f"Operand 1   : {operand1_bin} -> {val1}")
    print(f"Operand 2   : {operand2_bin} -> {val2}")
    print(f"Calculation : {val1} {operation_name} {val2} = {result}")
    
    # Convert result back to binary and pad it with leading zeros to maintain 3 bits
    print(f"Final Output: {bin(result)[2:].zfill(3)} (Binary)")

if __name__ == "__main__":
    alu_simulator()