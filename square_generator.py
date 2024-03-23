class MyException(Exception):
    pass


class SquareGenerator:
    def sq_squared(self, start, end):
        if start < end:
            raise MyException("start should be greater than end")
        res = []
        for i in range(start, end + 1):
            res.append(i ** 2)
        return res
