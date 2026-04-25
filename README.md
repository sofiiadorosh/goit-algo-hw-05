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


## 🏁 Fastest Algorithm Analysis (Based on Measured Data)

### 📄 Algorithm Usage text
The fastest algorithm for this text is:
- **Boyer–Moore**

It consistently shows the lowest execution time across both real and fake patterns.


### 📄 Data Structures text
The fastest algorithm for this text is:
- **Boyer–Moore**

It again outperforms KMP and Rabin–Karp in most cases.


## ✅ Conclusions

Based on all measurements across both texts:

- 🥇 **Boyer–Moore** → fastest overall
- 🥈 **Knuth–Morris–Pratt (KMP)** → stable but slower
- 🥉 **Rabin–Karp** → generally the slowest due to hashing overhead


## 🏁 Final Recommendation

- **Best overall performance:** Boyer–Moore (practical text searching)
- **Most reliable:** KMP (predictable linear performance)
- **Most flexible:** Rabin–Karp (useful for hashing / multi-pattern search)