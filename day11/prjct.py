import os

a = int(input("Enter an integer value for a: "))
if a <= 10:
    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "mah.text")

    with open(file_path, "w") as file:
        file.write(f"Value of a: {a}\n")
        file.write("File is created\n")
    print(f"File 'mah.text' has been created at {file_path}")
else:
    print("a is greater than 10. File not created.")
