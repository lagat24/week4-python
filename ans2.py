def error_handling():
    filename = input("Enter filename: ")
    try:
        with open(filename, "r") as f:
            print("✅ File opened successfully!")
            print("First 100 characters of file:\n")
            print(f.read(100)) 
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


error_handling()

