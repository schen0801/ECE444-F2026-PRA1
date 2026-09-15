class utils:
    """Utility functions grouped in a class.

    Methods are implemented as static methods to allow simple calls like
    `utils.reversed(x)` and `utils.formatter(x)`.
    """

    @staticmethod
    def reversed(number):
        """Reverse the digits of `number` and return as int.

        Accepts `int`, `float`, or numeric `str`. Floats and numeric strings
        are converted to `int` before reversing (dropping fractional part).
        Negative numbers preserve sign.
        """
        if isinstance(number, str):
            # allow strings like "123" or "123.0"
            n = int(float(number))
        elif isinstance(number, float):
            n = int(number)
        else:
            n = int(number)

        sign = -1 if n < 0 else 1
        s = str(abs(n))
        rev_s = s[::-1]
        # handle case where reversing yields leading zeros (e.g., 120 -> 21)
        return sign * int(rev_s) if rev_s else 0

    @staticmethod
    def formatter(number):
        """Return a tuple of (binary_str, octal_str) for `number`.

        Accepts `int`, `float`, or numeric `str`. Floats and numeric strings
        are converted to `int` (fractional part dropped). Returned strings
        do not include Python prefixes (`0b`, `0o`). Negative numbers include
        a leading '-' followed by the positive representation.
        """
        if isinstance(number, str):
            n = int(float(number))
        elif isinstance(number, float):
            n = int(number)
        else:
            n = int(number)

        if n < 0:
            binary = '-' + bin(-n)[2:]
            octal = '-' + oct(-n)[2:]
        else:
            binary = bin(n)[2:]
            octal = oct(n)[2:]

        return binary, octal
