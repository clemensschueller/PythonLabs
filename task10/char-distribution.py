def split_sequence_file():
    # Read the cleaned sequence file
    with open('preproinsulin-seq-clean.txt', 'r') as file:
        content = file.read().strip()
    
    # Split the sequence into different parts
    lsinsulin = content[:24]        # First 24 characters
    binsulin = content[24:54]       # Characters 25-54
    cinsulin = content[54:89]       # Characters 55-89
    ainsulin = content[89:110]      # Characters 90-110
    
    # Write each part to its respective file
    file_parts = {
        'lsinsulin-seq-clean.txt': lsinsulin,
        'binsulin-seq-clean.txt': binsulin,
        'cinsulin-seq-clean.txt': cinsulin,
        'ainsulin-seq-clean.txt': ainsulin
    }
    
    # Create each file and write the corresponding sequence
    for filename, sequence in file_parts.items():
        with open(filename, 'w') as file:
            file.write(sequence)
        print(f"Created {filename} with {len(sequence)} characters: {sequence}")

# Run the function
try:
    split_sequence_file()
    print("\nAll files have been created successfully!")
except FileNotFoundError:
    print("Error: preproinsulin-seq-clean.txt not found!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
