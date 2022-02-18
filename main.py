if __name__ == '__main__':
    INPUT_FILE = "inputs/03_BinaryDiagnostics.txt"
    with open(INPUT_FILE) as f:
        diagnosticfile = [binary_string for line in f if (binary_string := line.strip())]

    gamma = ''
    epsilon = ''
    num = len(diagnosticfile)

    for i in range(len(diagnosticfile[0])):
        num_ones = sum(int(diagnosticfile[j][i]) for j in range(num))
        if num_ones >= (num - num_ones):
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"

    print("Binary Diagnostics - Part 1 : ", int(epsilon, 2) * int(gamma, 2))