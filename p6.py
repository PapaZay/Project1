import sys

def read_sequences_from_file(file_path, min_length):
    sequences = []
    with open(file_path, 'r') as file:
        current_sequence = ""
        for line in file:
            line = line.strip().upper()  # converts to uppercase
            if line.startswith('>'):
                if current_sequence and len(current_sequence) >= min_length:
                    sequences.append(current_sequence)
                current_sequence = ""
            else:
                current_sequence += line
        if current_sequence and len(current_sequence) >= min_length:  # add the last sequence if it meets the length requirement
            sequences.append(current_sequence)
    return sequences

def determine_optimal_length(sequences):
    max_length = max(len(seq) for seq in sequences)
    return max_length

def format_sequences(sequences, optimal_length):
    formatted_sequences = []
    for seq in sequences:
        # trim sequences
        formatted_seq = seq[:optimal_length]
        formatted_sequences.append(formatted_seq)
    return formatted_sequences

def write_sequences_to_file(formatted_sequences, output_file):
    with open(output_file, 'w') as file:
        for i, seq in enumerate(formatted_sequences, 1):
            file.write(f"Sequence: {i}\n")
            file.write(seq + '\n')

def main():
    if len(sys.argv) != 4:
        print("Formatt: python3 script.py inputfile.txt outputfile.txt minimum_sequence_length")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    min_length = int(sys.argv[3])

    sequences = read_sequences_from_file(input_file, min_length)
    if not sequences:
        print("No sequences found in the file or all sequences are shorter than the specified minimum length.")
        return

    optimal_length = determine_optimal_length(sequences)
    formatted_sequences = format_sequences(sequences, optimal_length)

    write_sequences_to_file(formatted_sequences, output_file)
    print(f"Formatted sequences have been written to {output_file}.")

if __name__ == "__main__":
    main()

