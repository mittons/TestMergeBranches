
def compare_files(file1, file2):
    """Compares the contents of two files for exact match."""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        return content1 == content2

if __name__ == "__main__":
    result = compare_files('./tests/new_output.txt', './tests/base_output.txt')
    if result:
        print("The files are identical.")
    else:
        print("The files are different.")
