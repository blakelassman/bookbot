def count_characters(text):
    # Convert all uppercase letters to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_counts = {}
    
    # Iterate through each character in the text
    for char in text:
        # If the character is alphanumeric
        if char.isalpha():
            # Increment the count for the character in the dictionary
            char_counts[char] = char_counts.get(char, 0) + 1
    
    return char_counts

def count_words(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def generate_report(word_counts, char_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counts} words found in the document\n")
    
    # Sort character counts by occurrences in descending order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    # Open the file and read its contents
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    
    # Count words
    num_words = count_words(file_contents)
    
    # Count characters
    char_counts = count_characters(file_contents)
    
    # Generate and print the report
    generate_report(num_words, char_counts)

# Call the main function to run the program
main()