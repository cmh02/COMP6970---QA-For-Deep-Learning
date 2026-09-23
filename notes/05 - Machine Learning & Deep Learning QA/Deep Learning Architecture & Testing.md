---
title: "Deep Learning Architecture & Testing"
aliases:
  - "Deep Learning Testing"
  - "DL Architecture"
  - "Representation Learning"
  - "Neural Network QA"
tags:
  - comp6970
  - deep-learning
  - neural-networks
  - deep-learning-qa
course: "COMP6970 - QA for Deep Learning"
source_lectures:
  - "Lecture 15.pdf"
created: 2026-09-23
---

# Deep Learning Architecture & Testing

**Deep Learning (DL)** replaces manual, handcrafted feature engineering with hierarchical **representation learning**, composing layers of non-linear transformations to automatically discover abstractions from raw data.

---

## 1. Classical Machine Learning vs. Deep Learning

```mermaid
graph TD
    subgraph Classical["Classical Machine Learning"]
        C1[Raw Data: Pixels / Audio] --> C2[Human Handcrafted Feature Extraction: SIFT, HOG]
        C2 --> C3[Shallow Classifier: SVM, Random Forest]
        C3 --> C4[Output]
    end
    
    subgraph Deep["Deep Learning Paradigm"]
        D1[Raw Data: Pixels / Audio] --> D2[Layer 1: Low-level Edges / Textures]
        D2 --> D3[Layer 2: Intermediate Parts / Motifs]
        D3 --> D4[Layer 3: High-level Object Classes]
        D4 --> D5[End-to-End Prediction]
    end
```

### Representation Learning
- **Classical ML**: Depends heavily on domain experts to craft features. The quality of testing often focuses on feature extractor heuristics.
- **Deep Learning**: Learns intermediate representations end-to-end directly from raw sensory inputs.

---

## 2. Layer Composition & Neural Network Architecture

A deep neural network is mathematically modeled as a composite function $F(x)$:

$$ F(x) = (f_L \circ f_{L-1} \circ \dots \circ f_2 \circ f_1)(x) $$

```mermaid
flowchart LR
    Input["Input Vector x"] --> L1["Dense / Conv Layer 1: f1(x) = sigma(W1 x + b1)"]
    L1 --> L2["Hidden Layer 2: f2(h1)"]
    L2 --> L3["Hidden Layer 3: f3(h2)"]
    L3 --> Out["Output Layer: fL(h_L-1) -> y_pred"]
```

### Key Mathematical Components:
1. **Linear Transformation (Dense / Fully Connected Layer)**:
   $$ z = W x + b $$
   *(where $W$ is the weight matrix and $b$ is the bias vector)*.
2. **Non-Linear Activation Function ($\sigma$)**:
   $$ a = \sigma(z) $$
   *(e.g., ReLU, GeLU, Sigmoid, Softmax)*. Non-linearities allow the network to approximate arbitrary non-linear decision boundaries (Universal Approximation Theorem).
3. **Depth**: Composing many layers ($L \gg 1$) allows networks to build hierarchical concepts, where earlier layers capture local primitives and deeper layers capture abstract global semantics.

---

## 3. Unique Quality Assurance & Testing Challenges for Deep Learning

Testing Deep Neural Networks differs fundamentally from testing traditional software due to the following characteristics:

```mermaid
mindmap
  root((Deep Learning QA Challenges))
    The Oracle Problem
      No explicit ground truth for arbitrary synthetic inputs
      Solution: Metamorphic & Differential Testing
    Non-Determinism
      GPU floating-point non-associativity
      Stochastic training & initialization
    Black-Box Complexity
      Billions of parameters
      Lack of explainable control-flow paths
    Distribution Shift
      Model fails when test data diverges from training distribution
```

### Summary of Testing Strategies for DL:
1. **Adversarial Robustness Testing**: Evaluating whether imperceptible input perturbations ($\delta$) cause catastrophic classification flips (e.g., FGSM, PGD attacks).
2. **Metamorphic Invariance Testing**: Applying transformations like rotations, translations, lighting changes, or blur (see [[Metamorphic Testing]]).
3. **Neuron & Layer Coverage**: Extending traditional structural code coverage ([[Code Coverage Criteria]]) to neuron activation metrics (e.g., DeepXplore neuron coverage).
4. **Differential Execution**: Validating cross-framework numerical stability between PyTorch, ONNX, and TensorRT (see [[Differential Testing]]).

---

## Related Notes
- [[Machine Learning Foundations for QA]] — Loss functions, generalization, overfitting, and bias/variance
- [[Metamorphic Testing]] — Core technique for testing deep learning systems
- [[Differential Testing]] — Cross-hardware and cross-engine testing for neural networks

---

## Lecture Sources & History
- **Lecture 15** (`Lecture 15.pdf`) — Representation learning vs handcrafted features, layer composition, dense connections, and deep neural architectures.
