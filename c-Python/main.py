import ctypes

tutorialc = ctypes.CDLL("./tutorial.so")


def HelloFWorld():
    tutorialc.say_hello()


class Tutorial:
    def __init__(self) -> None:
        HelloFWorld()







if __name__ == "__main__":
    Tutorial()