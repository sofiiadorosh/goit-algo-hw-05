import timeit

from algorithms import boyer_moore_search, kmp_search, rabin_karp_search


def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return fh.read()

    except FileNotFoundError:
        print("File not found")
        return []

    except (IndexError, ValueError):
        print("File format is incorrect")
        return []


def measure(search_algorithm, text, pattern):
    return timeit.timeit(lambda: search_algorithm(text, pattern), number=5) / 5


def compare_search_algorithm():
    algorithm_usage = read_file("articles/algorithm_usage.txt")
    data_structures = read_file("articles/data_structures.txt")

    real_pattern = "пошук"
    fake_pattern = "космос"

    print(f"{'Algorithm':<25} | {'Article':<20} | {'Pattern':<10} | {'Time (s)':<10}")
    print("-" * 75)

    for text, text_name in [
        (algorithm_usage, "Algorithm Usage"),
        (data_structures, "Data Structures")
    ]:
        for pattern, pattern_name in [
            (real_pattern, "Real"),
            (fake_pattern, "Fake")
        ]:

            time_boyer_moore_search = measure(boyer_moore_search, text, pattern)
            print(f"{'Boyer-Moore':<25} | {text_name:<20} | {pattern_name:<10} | {time_boyer_moore_search:.6f}")

            time_kmp = measure(kmp_search, text, pattern)
            print(f"{'Knuth-Morris-Pratt':<25} | {text_name:<20} | {pattern_name:<10} | {time_kmp:.6f}")

            time_rabin_karp_search = measure(rabin_karp_search, text, pattern)
            print(f"{'Rabin-Karp':<25} | {text_name:<20} | {pattern_name:<10} | {time_rabin_karp_search:.6f}")

            print("-" * 75)


if __name__ == "__main__":
    compare_search_algorithm()