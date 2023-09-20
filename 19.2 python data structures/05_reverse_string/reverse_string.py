def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # arr = [char for char in phrase]
    arr = list(phrase)
    size = len(arr)
    for i in range(0, size//2):
        temp = arr[i]
        arr[i] = arr[size - 1 - i]
        arr[size - 1 - i] = temp
    return "".join(arr)
