from timeit import timeit
from tasks import add


def call_task():
    result = add.delay(4, 4)
    print('answer is:', result.get())
    result.forget()


if __name__ == "__main__":
    t = timeit('call_task()', number=1, globals=globals())
    print('task executing:', t)
