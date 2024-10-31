import os
import glob


def show_docs():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the docs.txt file
    docs_path = os.path.join(current_dir, "docs.txt")

    # Check if the documentation file exists
    if os.path.exists(docs_path):
        # Load and read the text file
        with open(docs_path, "r") as file:
            text_content = file.read()

        # Print the plain text output
        print(text_content)
    else:
        print("Documentation file not found.")

def list_files():
    # Get the directory of the current script file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all .py files in the same directory as the script
    py_files = sorted(glob.glob(os.path.join(current_dir, "*.py")))

    # Print each file name and its description
    for file_path in py_files:
        file_name = os.path.basename(file_path)
        description = "No description available"
        
        # Read the file and look for a line defining `description`
        with open(file_path, "r") as f:
            for line in f:
                if line.startswith("description ="):
                    # Extract the description value
                    description = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
        
        print("\n")
        print(f"{file_name}")
        print(f"Description: {description}\n")

def main():
    # Prompt the user to see the documentation
    user_input = input("Would you like to see the documentation? (y/n): ").strip().lower()
    
    if user_input == 'y':
        show_docs()
    else:
        print("Okay, not displaying the documentation.")
    
    # Prompt the user to see the documentation
    user_input = input("Would you like to see the available files? (y/n): ").strip().lower()
    
    if user_input == 'y':
       list_files()
    else:
        print("Okay, not listing available files.")

if __name__ == "__main__":
    main()