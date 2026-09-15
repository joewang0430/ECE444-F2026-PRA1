class utils:
    def reversed(self, number):
        # I added the error handler just in case the input type is incorrect
        if not isinstance(number, int):
            raise TypeError("Input must be the type of integer") 
        return int(str(number)[::-1])

    def formatter(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be the type of integer")
        return bin(number), oct(number)