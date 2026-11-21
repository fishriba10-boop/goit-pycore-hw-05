"""Task 1: Fibonacci numbers with a cache stored in a closure."""


def caching_fibonacci():
    """Create and return the fibonacci(n) function with its own cache."""
    cache = {}  # the closure keeps this dictionary between calls

    def fibonacci(n):
        """Return the n-th Fibonacci number, using the cache when possible."""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Not in the cache yet: calculate recursively and save the result
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
