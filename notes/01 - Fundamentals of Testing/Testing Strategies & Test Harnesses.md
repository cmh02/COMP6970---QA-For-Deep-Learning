---
title: "Testing Strategies & Test Harnesses"
aliases:
  - "Testing Strategies"
  - "Test Harnesses"
  - "Black-Box vs White-Box Testing"
  - "Test Oracles"
tags:
  - comp6970
  - testing-strategies
  - test-architecture
course: "COMP6970 - QA for Deep Learning"
source_lectures:
  - "Lecture 2 - Basic Testing Concepts"
created: 2026-09-23
---

# Testing Strategies & Test Harnesses

Software testing strategies determine how tests are conceived, structured, executed, and evaluated relative to the system's internal implementation details.

---

## 1. Box Testing Strategies (Visibility-Based)

Testing techniques are categorized by the level of visibility the tester or automated test tool has into the internal source code:

```mermaid
graph TD
    subgraph BlackBox["Black-Box Testing"]
        B1["Input -> [ Hidden Internal Logic ] -> Output"]
        B2["Specification & Requirements-driven"]
    end
    subgraph GreyBox["Grey-Box Testing"]
        G1["Input -> [ Partial Internal Visibility ] -> Output"]
        G2["Structural feedback (e.g. branch coverage)"]
    end
    subgraph WhiteBox["White-Box Testing"]
        W1["Input -> [ Full Code & Path Visibility ] -> Output"]
        W2["Control-flow & data-flow driven"]
    end
```

### Comparative Summary

| Strategy | Visibility | Key Techniques | Primary Advantages | Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Black-Box** | Zero internal code knowledge | [[Input Space Partitioning & Combinatorial Testing#Equivalence Partitioning\|Equivalence Partitioning]], [[Input Space Partitioning & Combinatorial Testing#Boundary Value Analysis (BVA)\|Boundary Value Analysis]] | Unbiased; tests user requirements directly; code-agnostic | Cannot identify dead code or hidden logic paths |
| **White-Box** | Full internal source code visibility | [[Control Flow Graphs (CFG)|CFG Analysis]], [[Code Coverage Criteria|Code Coverage]], [[Modified Condition Decision Coverage (MCDC)|MC/DC]] | Thoroughly exercises implementation logic and hidden edge cases | Labor intensive; does not reveal missing specification features |
| **Grey-Box** | Partial visibility (e.g., architecture, byte instrumentation) | [[Fuzzing#2. Grey-Box Fuzzing\|Coverage-guided Fuzzing]], State-machine testing | Combines speed of black-box with guidance of white-box | Requires lightweight instrumentation |

---

## 2. Test Cases, Test Suites, and Test Fixtures

Modern automated testing relies on modular abstractions to manage test inputs and execution state.

```mermaid
classDiagram
    class TestSuite {
        +List~TestCase~ testCases
        +run()
    }
    class TestCase {
        +TestInput input
        +ExpectedOutput expected
        +TestOracle oracle
        +execute()
    }
    class TestFixture {
        +setUp()
        +tearDown()
    }
    TestSuite "1" *-- "*" TestCase
    TestCase ..> TestFixture : uses
```

### Components

> [!definition] Test Case
> A set of test inputs, execution preconditions, and expected outcomes developed for a particular objective (such as exercising a specific program path or verifying compliance with a requirement).
> 
> Formally, a test case consists of:
> $$ \text{TestCase} = \langle \text{Input Data } (x), \text{Preconditions } (P), \text{Expected Output } (y), \text{Postconditions } (Q) \rangle $$

> [!definition] Test Suite
> A collection of test cases grouped together for execution purposes (e.g., Smoke Test Suite, Regression Test Suite, Integration Test Suite).

> [!definition] Test Harness & Runner
> A software framework that configures the execution environment, executes test suites, records test outcomes, and reports passes/failures.

> [!definition] Test Fixture
> The fixed baseline state required to run a test repeatedly and deterministically. Managed via setup (`setUp()`) and teardown (`tearDown()`) routines.

---

## 3. The Test Oracle

A **Test Oracle** is the mechanism used to determine whether the software passed or failed a given test execution.

$$ \text{Oracle}(x, \text{actual\_output}) \to \{\text{PASS}, \text{FAIL}\} $$

```mermaid
flowchart LR
    Input[Test Input x] --> SUT[System Under Test f]
    SUT --> Actual[Actual Output y = f x]
    Actual --> Oracle{Test Oracle}
    Expected[Expected Output y* / Specification] --> Oracle
    Oracle -->|Match| Pass[PASS]
    Oracle -->|Mismatch| Fail[FAIL]
```

### Types of Oracles
1. **Direct Value Assertions**: Exact match against pre-calculated values (e.g., `assertEqual(4, square(2))`).
2. **Implicit / Crash Oracles**: Checking that the program runs without crashing, memory leaks, or unhandled exceptions (standard in [[Fuzzing]]).
3. **Property / Contract Oracles**: Invariants that must hold across all outputs (e.g., $y \ge 0$, sorted output is monotonic).
4. **Relational Oracles**: Comparing relative output shifts between transformed inputs (see [[Metamorphic Testing]]).

> [!warning] The Oracle Problem
> In many complex domains (machine learning, scientific computing, graphics rendering, search algorithms), calculating the expected output manually is impossible or computationally infeasible. This is known as the **Oracle Problem**.

---

## Related Notes
- [[Software Testing Foundations]] — Error, fault, failure definitions and testing economics
- [[Unit Testing & xUnit Frameworks]] — Concrete implementation of test runners and suites
- [[Metamorphic Testing]] — Advanced solution to the Oracle Problem

---

## Lecture Sources & History
- **Lecture 2** (`Lecture 2 - Basic Testing Concepts.pdf`) — Black-box, white-box, grey-box testing, test cases, test suites, test runners, and test oracles.
