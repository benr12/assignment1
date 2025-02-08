from functools import lru_cache
import time
import matplotlib.pyplot as plt

timing_data = []
fib_indices = []

def measure_time(func):
    def wrapped(n):
        begin = time.perf_counter()
        outcome = func(n)
        finish = time.perf_counter()
        duration = finish - begin
        
        timing_data.append(duration)
        fib_indices.append(n)
        
        print(f"Computed in {duration:.8f}s: fib({n}) -> {outcome}")
        return outcome
    return wrapped

@lru_cache
@measure_time
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    fibonacci(100)
    
    ordered_points = [(fib_indices[j], timing_data[j]) for j in range(len(fib_indices))]
    ordered_points.sort()

    sorted_x = [pair[0] for pair in ordered_points]
    sorted_y = [pair[1] for pair in ordered_points]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_x, sorted_y)
    
    plt.title('Fibonacci Computation Time')
    plt.xlabel('Fibonacci Sequence Index')
    plt.ylabel('Time (seconds)')
    plt.grid(True, alpha=0.5)

    plt.tight_layout()
    plt.savefig('fib_timing.png')
    plt.show()
