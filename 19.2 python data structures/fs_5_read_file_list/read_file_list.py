def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    DIR = "/home/tya/github/python/19.2 python data structures/fs_5_read_file_list/"
    with open(DIR + filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(f"- {line.strip()}")