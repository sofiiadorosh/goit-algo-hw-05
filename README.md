## 📊 Search Algorithms Efficiency Analysis

This report presents an empirical comparison of three string-search algorithms:
* **Boyer–Moore**
* **Knuth–Morris–Pratt (KMP)**
* **Rabin–Karp**

The experiments were conducted on two different text sources with both a **real pattern (“пошук”)** and a **fake pattern (“космос”)**, allowing analysis of both successful and unsuccessful search cases.


## ⚖️ Algorithm Comparison

### 1. Boyer–Moore Algorithm
Boyer–Moore generally showed the best performance in most cases, especially on longer texts.

**Why it performs well:**
- Skips large portions of the text using heuristics (bad character + good suffix rules)
- Reduces the number of character comparisons in practice

**Best suited for:**
- Large text files
- Real-world search problems where patterns are not highly repetitive


### 2. Knuth–Morris–Pratt (KMP)
KMP demonstrated stable and predictable performance across all inputs.

**Strengths:**
- Never rechecks characters in the text
- Guarantees linear complexity **O(n + m)**

**Behavior:**
- Consistent execution time for both successful and failed searches

**Best suited for:**
- Systems where predictable performance is important
- Repeated pattern matching tasks


### 3. Rabin–Karp Algorithm
Rabin–Karp showed competitive but less stable performance.

**Key characteristics:**
- Uses hashing for pattern matching
- Performance depends on hash collisions

**Observations:**
- Can be fast for simple cases
- May slow down due to additional verification steps

**Best suited for:**
- Multi-pattern searching
- Cases where hashing is advantageous


## 🔍 Real vs Fake Pattern Impact

- **Real pattern (“пошук”)**: may take longer if it appears frequently in text
- **Fake pattern (“космос”)**: often faster due to early mismatches and quick rejection


## ✅ Conclusions

No single algorithm is universally optimal:

- **Boyer–Moore** → fastest in real-world usage  
- **KMP** → most stable and predictable  
- **Rabin–Karp** → useful for specialized hashing-based scenarios  


## 🏁 Final Recommendation

- **Best overall performance:** Boyer–Moore (practical text searching)
- **Most reliable:** KMP (predictable linear performance)
- **Most flexible:** Rabin–Karp (useful for hashing / multi-pattern search)