from abc import ABCMeta,abstractstaticmethod


class IChair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimensions():
        """The Chair Interface"""


class BigChair(IChair):

    def __init__(self):
        self.height=80
        self.width=80
        self.depth=80

    def get_dimensions(self):
        return {"height":self.height, "width":self.width, "depth":self.depth}


class MediumChair(IChair):

    def __init__(self):
        self.height=70
        self.width=70
        self.depth=70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallChair(IChair):

    def __init__(self):
        self.height=60
        self.width=60
        self.depth=60

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory():

    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype== "BigChair":
                return BigChair()
            if chairtype== "MediumChair":
                return MediumChair()
            if chairtype == "SmallChair":
                return SmallChair()
            raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    CHAIR=ChairFactory.get_chair("BigChair")
    print(f"{CHAIR.__class__}:{CHAIR.get_dimensions()}")
    CHAIR=ChairFactory.get_chair("SmallChair")
    print(f"{CHAIR.__class__}:{CHAIR.get_dimensions()}")