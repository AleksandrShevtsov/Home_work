def countdown(n):
    print("Starting countdown")
    while n > 0:
        if n == 5:
            return "Stop"
        yield n
        n -= 1
    return "Done"

gen = countdown(10)
try:
    while True:
        value = next(gen)
        print(value)
except StopIteration as e:
    print(f"Generator finished with message: {e.value}")




def alternating_numbers():
    while True:
        for number in [10, 20, 30]:
            yield number

gen = alternating_numbers()
for _ in range(10):
    print(next(gen))



