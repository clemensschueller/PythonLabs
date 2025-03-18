def clean_sequence_file(input_file, output_file):
    # Read the original file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Remove "ORIGIN" and "//"
    content = content.replace('ORIGIN', '').replace('//', '')
    
    # Remove line numbers and extra spaces
    cleaned_content = ''
    for line in content.split('\n'):
        # Skip empty lines
        if line.strip():
            # Remove line numbers and spaces, convert to lowercase
            cleaned_line = ''.join(char for char in line if char.isalpha())
            cleaned_content += cleaned_line.lower()
    
    # Write the cleaned content to a new file
    with open(output_file, 'w') as file:
        file.write(cleaned_content)
    
    print(f"Cleaned sequence has been saved to {output_file}")

# Use the function
input_file = "preproinsulin-seq.txt"
output_file = "preproinsulin-seq-clean.txt"

clean_sequence_file(input_file, output_file)
