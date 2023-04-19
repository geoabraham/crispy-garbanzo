def timed(reps):
    def dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(f'Function {fn.__name__} took an average of {avg_elapsed}')
            return result

        return inner

    return dec


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


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@counter
@timed(5)
@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


@counter
@timed(5)
@logged
def compute_powers(n, *, start=1, end):
    # using a list comprehension
    return [n ** i for i in range(start, end)]


@memoize
def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


print(fib(2))
# fact(20000)
# compute_powers(2, end=20000)
