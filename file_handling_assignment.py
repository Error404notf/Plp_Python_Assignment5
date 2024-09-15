# File creation and writing to 'my_file.txt'
try:
    # Open 'my_file.txt' in write mode ('w')
    with open('my_file.txt', 'w') as file:
        # Write three lines of text to the file
        file.write("This is the first line of the file.\n")
        file.write("Here's the second line, with a number: 12345.\n")
        file.write("And the third line, including some text and numbers: 67890.\n")

    print("File 'my_file.txt' created and written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while creating or writing to the file: {e}")

finally:
    print("File creation and writing operation completed.")

# File reading and displaying its contents
try:
    # Open 'my_file.txt' in read mode ('r')
    with open('my_file.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Display the contents on the console
        print("\nContents of 'my_file.txt':")
        print(contents)

except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file: {e}")

finally:
    print("File reading operation completed.")

# File appending to 'my_file.txt'
try:
    # Open 'my_file.txt' in append mode ('a')
    with open('my_file.txt', 'a') as file:
        # Append three additional lines of text to the file
        file.write("Appending a new line to the file.\n")
        file.write("Another line added, with more text and a number: 54321.\n")
        file.write("Final appended line with additional information.\n")

    print("Additional lines appended to 'my_file.txt' successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while appending to the file: {e}")

finally:
    print("File appending operation completed.")
