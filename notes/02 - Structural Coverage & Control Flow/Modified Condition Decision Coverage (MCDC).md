---
title: "Modified Condition Decision Coverage (MC/DC)"
aliases:
  - "MC/DC"
  - "MCDC"
  - "Modified Condition / Decision Coverage"
tags:
  - comp6970
  - structural-testing
  - mcdc
  - safety-critical
course: "COMP6970 - QA for Deep Learning"
source_lectures:
  - "Lecture 6.pdf"
created: 2026-09-23
---

# Modified Condition Decision Coverage (MC/DC)

**Modified Condition / Decision Coverage (MC/DC)** is a white-box test adequacy criterion specifically designed for safety-critical systems (e.g., DO-178C for commercial avionics, ISO 26262 for automotive).

It provides high confidence in complex Boolean logic while requiring only a **linear** number of test cases ($N + 1$) rather than the **exponential** ($2^N$) test cases demanded by Multiple Condition Coverage.

---

## 1. Core Terminology

- **Decision**: A Boolean expression composed of conditions combined with logical operators (`AND`, `OR`, `NOT`) that determines program control flow (e.g., `(A AND B) OR C`).
- **Condition**: A leaf-level Boolean variable or relational comparison that cannot be further decomposed (e.g., `A`, `x > 5`).

---

## 2. The MC/DC Requirements

To achieve 100% MC/DC coverage, a test suite must satisfy four criteria:

1. Every **Decision** has taken all possible outcomes (`True` and `False`) at least once.
2. Every **Condition** in the decision has taken all possible outcomes (`True` and `False`) at least once.
3. Every **entry and exit point** has been invoked.
4. **Independent Influence Property**: Each condition must be shown to **independently affect** the overall decision outcome by holding all other conditions constant while toggling that single condition.

> [!definition] Independent Influence Condition
> For each condition $C_i$, there must exist a pair of test cases $T_1$ and $T_2$ such that:
> - $C_i$ has value `True` in $T_1$ and `False` in $T_2$.
> - All other conditions $C_j$ ($j \ne i$) remain identical (or do not affect the decision outcome).
> - The entire decision evaluates to `True` in $T_1$ and `False` in $T_2$ (or vice-versa).

---

## 3. Test Pair Selection & The $N+1$ Rule

For a decision with $N$ conditions:
- Full exhaustive truth table testing requires $2^N$ test cases.
- **MC/DC requires a minimum of $N + 1$ test cases** (and at most $2N$).

### Concrete Example: Decision $D = (A \lor B) \land C$

Here $N = 3$ conditions: $A, B, C$. Exhaustive testing would require $2^3 = 8$ tests.

Let's evaluate the full truth table:

| Test # | $A$ | $B$ | $C$ | Decision $D = (A \lor B) \land C$ | Notes |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | `T` | `T` | `T` | `T` | |
| **2** | `T` | `F` | `T` | `T` | Pair for $B$ with Test 1? No ($D$ doesn't flip) |
| **3** | `F` | `T` | `T` | `T` | |
| **4** | `F` | `F` | `T` | `F` | **Key test** |
| **5** | `T` | `T` | `F` | `F` | |
| **6** | `T` | `F` | `F` | `F` | |
| **7** | `F` | `T` | `F` | `F` | |
| **8** | `F` | `F` | `F` | `F` | |

### Finding Independent Test Pairs:
1. **For Condition $A$**:
   - Compare **Test 2** (`T, F, T` $\to D = \text{True}$) and **Test 4** (`F, F, T` $\to D = \text{False}$).
   - $B$ is held at `F`, $C$ is held at `T`. Toggling $A$ directly changes $D$.
   - **Independence Pair for $A$**: $(2, 4)$.
2. **For Condition $B$**:
   - Compare **Test 3** (`F, T, T` $\to D = \text{True}$) and **Test 4** (`F, F, T` $\to D = \text{False}$).
   - $A$ is held at `F`, $C$ is held at `T`. Toggling $B$ directly changes $D$.
   - **Independence Pair for $B$**: $(3, 4)$.
3. **For Condition $C$**:
   - Compare **Test 2** (`T, F, T` $\to D = \text{True}$) and **Test 6** (`T, F, F` $\to D = \text{False}$).
   - $A$ is held at `T`, $B$ is held at `F`. Toggling $C$ directly changes $D$.
   - **Independence Pair for $C$**: $(2, 6)$.

### Minimal Test Suite for 100% MC/DC:
Selecting $\{ \text{Test 2}, \text{Test 3}, \text{Test 4}, \text{Test 6} \}$ gives:
- Test count = $4 = N + 1 = 3 + 1$.
- Achieves 100% MC/DC coverage!

---

## 4. MC/DC Adequacy Score Formula

$$ \text{MC/DC Score} = \frac{\text{Number of Conditions with Valid Test Pairs}}{\text{Total Number of Conditions}} \times 100\% $$

> [!tip] Why MC/DC is Standard in Aerospace (DO-178C)
> When a flight-control system has a safety decision with 10 conditions ($N = 10$), exhaustive testing requires $2^{10} = 1,024$ tests per branch. MC/DC guarantees every condition has observable independent influence with only $10 + 1 = 11$ test cases!

---

## Related Notes
- [[Control Flow Graphs (CFG)]] — CFG representation of conditional decisions
- [[Code Coverage Criteria]] — Subsumption hierarchy (MC/DC subsumes Branch and Statement coverage)
- [[Input Space Partitioning & Combinatorial Testing]] — Black-box combinatorial approaches

---

## Lecture Sources & History
- **Lecture 6** (`Lecture 6.pdf`) — Modified Condition/Decision Coverage definition, independence influence property, test pair selection, and $N+1$ formula.
