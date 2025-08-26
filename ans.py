def file_read_write():
    try:

        input_file = input("Enter the name of the file to read: ")

        with open(input_file, "r") as f:
            content = f.read()

        modified_content = content.upper()

        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified file saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


file_read_write()
