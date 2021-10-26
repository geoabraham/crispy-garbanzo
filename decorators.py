def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f'Function {fn.__name__} took {elapsed}')
        return result

    return inner


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        return result

    return inner


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} was called {count} times')
        return fn(*args, **kwargs)

    return inner


@counter
@timed
@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


@counter
@timed
@logged
def compute_powers(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


fib_cache = {1: 1, 2: 1}


def fib(n):
    if n not in fib_cache:
        print(f'Calculating fib({n})')
        fib_cache[n] = fib(n-1) + fib(n-2)

    return fib_cache[n]


print(fib(100))
# fact(20000)
# compute_powers(2, end=20000)
