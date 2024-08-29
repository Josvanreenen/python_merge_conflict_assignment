def calculate(operation, a, b):
    if operation == "addition":
        return a + b
    # Placeholder for more operations
    else:
        return "Unsupported operation"

def main():
    # Test case
    result = calculate("addition", 10, 5)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()