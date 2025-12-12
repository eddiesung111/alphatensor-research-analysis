# AlphaTensor: Deep Reinforcement Learning for Matrix Multiplication

## 📄 Project Overview
This repository contains a technical analysis and reproduction study of DeepMind's "AlphaTensor" paper (*Nature, 2022*). The research focuses on how Deep Reinforcement Learning (specifically Monte Carlo Tree Search) can be used to discover novel algorithms for matrix multiplication that are more efficient than the standard Strassen algorithm.

## 📂 Contents
* **`AlphaTensor_Analysis.pdf`**: Full technical report dissecting the tensor decomposition problem.
* **`Presentation_Slides.pdf`**: Summary of findings presented to [Your University Class Name].

## 🧠 Key Concepts Analyzed
* **Tensor Game:** Mapping algorithmic discovery to a 3D tensor decomposition game.
* **RL Agent:** How AlphaZero was adapted to minimize the rank of the tensor (minimizing scalar multiplications).
* **Strassen's Algorithm:** Comparative analysis of O(n^2.81) vs AlphaTensor's findings.

## 📂 Project Structure

```text
.
├── AlphaTensor_Analysis_Report.pdf   # Full technical breakdown (Overleaf)
├── Presentation_Slides.pdf           # Summary slides
├── src/
│   └── complexity_analysis.py        # Python script visualizing O(N) scaling
├── img/
│   └── complexity_comparison.png     # Generated visualization graph
├── requirements.txt                  # Python dependencies
└── README.md
```

## 🔗 Original Paper
* Fawzi et al. (2022). *Discovering faster matrix multiplication algorithms with reinforcement learning*. Nature.
