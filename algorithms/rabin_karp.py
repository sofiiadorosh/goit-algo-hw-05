def polynomial_hash(pattern, base=256, modulus=101):
    n = len(pattern)
    hash_value = 0
    for i, char in enumerate(pattern):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(text, pattern):
    patern_length = len(pattern)
    text_length = len(text)

    base = 256
    modulus = 101

    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(text[:patern_length], base, modulus)

    h_multiplier = pow(base, patern_length - 1) % modulus

    for i in range(text_length - patern_length + 1):
        if pattern_hash == current_slice_hash:
            if text[i:i + patern_length] == pattern:
                return i

        if i < text_length - patern_length:
            current_slice_hash = (current_slice_hash - ord(text[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(text[i + patern_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
