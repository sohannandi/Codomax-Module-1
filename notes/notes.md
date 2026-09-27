# Module 1 — Learning Notes: AI & Python

These notes cover AI, ML, and Deep Learning fundamentals, plus core Python
programming concepts needed throughout the internship.

---

## 1. Artificial Intelligence (AI)

**Artificial Intelligence (AI)** is the broad field of building machines
that can perform tasks that normally require human intelligence:
perception, reasoning, learning, problem-solving, and so on.

### Branches of AI
- **Narrow AI (Weak AI):** Solves one specific task (e.g., spam filters,
  voice assistants, recommendation engines).
- **General AI (Strong AI):** Hypothetical systems with human-level
  reasoning across any task (still largely theoretical).
- **Superintelligence:** A hypothetical AI that surpasses humans in
  every intellectual domain (speculative).

### AI techniques
- Search & optimization
- Knowledge representation & reasoning
- Planning & scheduling
- Natural Language Processing (NLP)
- Computer Vision
- Robotics

---

## 2. Machine Learning (ML)

**Machine Learning** is a subset of AI where computers learn patterns
from data rather than being explicitly programmed for every rule.

### How it works
Instead of coding rules, we:
1. Feed data into a model.
2. The model learns a statistical function mapping inputs → outputs.
3. We use the model to predict new outputs.

### Types of ML
| Type | Goal | Example |
|------|------|---------|
| Supervised Learning | Learn from labeled examples | Predict house prices, classify spam |
| Unsupervised Learning | Find hidden structure in data | Customer segmentation, topic modeling |
| Semi-supervised Learning | Mix of labeled + unlabeled data | Web content classification |
| Reinforcement Learning | Learn by trial-and-error with rewards | Game playing (AlphaGo), robotics |

### Common algorithms
- Linear / Logistic Regression
- Decision Trees / Random Forests
- K-Means Clustering
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Artificial Neural Networks

### Typical ML workflow
1. Define the problem & success metric.
2. Collect and label data.
3. Clean & preprocess data.
4. Split into train / validation / test sets.
5. Choose a model.
6. Train the model.
7. Evaluate performance.
8. Tune hyperparameters.
9. Deploy.

---

## 3. Deep Learning (DL)

**Deep Learning** is a subset of ML that uses **artificial neural
networks with many layers ("deep" networks) to learn hierarchical
representations of data.

### Neural networks — the big picture
- **Neuron:** a small unit that computes `activation(w·x + b)`.
- **Hidden layers:** stacked layers that learn features automatically.
- **Training:** minimize a loss function using gradient descent &
  backpropagation.

### Why deep learning?
- Learns features directly from raw data (images, text, audio).
- Excels at unstructured data.
- Scales well with large datasets and compute.

### Common architectures
| Type | Handles | Example models |
|------|--------|----------------|
| CNN (Convolutional NN) | Images / spatial data | ResNet, VGG |
| RNN / LSTM / GRU | Sequences (text, time) | Transformers, BERT |
| GAN | Generate new data | Image generation |
| Autoencoders | Compression / denoising | Anomaly detection |

**Relationship summary:**  
AI ⊃ ML ⊃ DL

---

## 4. Real-world AI applications
- **Healthcare:** disease detection, drug discovery.
- **Finance:** fraud detection, algorithmic trading.
- **Retail:** recommendation engines, demand forecasting.
- **Transportation:** autonomous vehicles, route optimization.
- **Customer service:** chatbots and virtual assistants.
- **Manufacturing:** predictive maintenance, quality control.

---

## 5. Python fundamentals

### 5.1 Variables & Data Types
- `int`, `float`, `str`, `bool`
- `None` for missing values.
- Type conversion: `int("3")`, `str(3.14)`.
- `type()` to inspect the type.

### 5.2 Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//` (floor), `%` (modulo), `**` (power)
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`, etc.

### 5.3 Conditional statements
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

### 5.4 Loops
- `for` iterates over a sequence (list, range, string).
- `while` repeats while a condition is true.
- `break` exits a loop; `continue` skips an iteration.

### 5.5 Lists
- Ordered, mutable collections: `colors = ["red", "green", "blue"]`
- Indexing: `colors[0]`; slicing: `colors[1:3]`
- Methods: `append()`, `insert()`, `remove()`, `pop()`, `len()`, `sort()`
- List comprehensions for concise transformations:
  `[x * 2 for x in range(5)]`

### 5.6 Functions
- Defined with `def`; take arguments and may `return` values.
- Parameters can have default values.
- Use functions to avoid repetition (DRY: Don't Repeat Yourself).

### 5.7 Input / Output
- `input("Prompt: ")` reads user input as a string.
- `print()` outputs values; supports f-strings:
  `print(f"Total = {total}")`

### 5.8 Error handling (try/except)
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid number.")
```

### 5.9 File I/O (preview of Module 2)
- `open("file.txt", "r")` to read; `"w"` to write.
- The `with` statement auto-closes files.
- `json` module serializes data to/from JSON.

---

## 6. Setting up Python
1. Download from [python.org](https://www.python.org/) (or use the
   pre-built bundle in the internship VM).
2. Verify: `python --version` (or `python3` on macOS/Linux).
3. (Optional) Create a virtual environment:
   `python -m venv env` then activate it.
4. Install packages: `pip install numpy pandas matplotlib`

---

## 7. Key takeaways
- AI is the big umbrella; ML learns from data; DL uses deep neural nets.
- Python is the lingua franca of AI/ML thanks to libraries.
- Clean, readable code matters more than clever tricks.
- Always handle user input safely to avoid crashes.

**Next:** apply these concepts to a mini project in Module 2.
