<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=wave&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=Graph%20Search%20Engine&fontSize=42&fontColor=white&fontAlignY=42&fontAlign=50&desc=Uninformed%20Search%20Algorithm%20Library&descAlignY=62&descAlign=50&descSize=18&animation=fadeIn" alt="Header" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-2563EB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithms-BFS_|_DFS_|_IDDFS-FF6F00?style=for-the-badge&logo=thealgorithms&logoColor=white" alt="Algorithms" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-059669?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Production Ready" />
  <img src="https://img.shields.io/badge/License-MIT-8B5CF6?style=for-the-badge&logo=bookstack&logoColor=white" alt="MIT" />
</p>

<p align="center">
  <h2>Production-grade library for breadth-first, depth-first, and iterative deepening search — the foundation of intelligent graph traversal</h2>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=24&duration=3000&pause=500&color=2563EB&center=true&vCenter=true&width=700&lines=Breadth-First+Search+(BFS);Depth-First+Search+(DFS);Iterative+Deepening+DFS+(IDDFS);Complete+%7C+Optimal+%7C+Efficient;Graph+Visualization+with+NetworkX" alt="Typing animation" />
</p>

<br/>

<p align="center">
  <a href="https://github.com/MALULEKE-KS"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://za.linkedin.com/in/kurhula-success-maluleke-32153231a"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:kurhula04s@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://komarev.com/ghpvc/?username=MALULEKE-KS&style=for-the-badge&color=2563EB&label=Views" alt="Profile views" />
</p>

---

<br/>

## About This Project

> *"Building practical digital systems that solve real-world challenges"*

This is a **production-grade uninformed search algorithm library** built as part of my BSc Computer Science & Mathematics Artificial Intelligence module. The system implements three fundamental graph traversal algorithms — **BFS**, **DFS**, and **IDDFS** — forming the foundation for intelligent pathfinding in complex networks.

Where basic implementations treat search algorithms as isolated functions, this library provides a complete engineering solution with type safety, error handling, visualization, and comprehensive documentation.

### System Architecture

| Phase | Focus |
| :--- | :--- |
| **1. Algorithm Design** | Clean implementations with optimal time/space complexity |
| **2. Type Safety** | Full type hints and input validation |
| **3. Visualization** | NetworkX-powered graph rendering |
| **4. Testing** | Verified against binary tree benchmark |

---

## Currently

| | |
| :--- | :--- |
| **Project** | Graph Search Engine — Uninformed Search Library |
| **Module** | CMPG 313 — Artificial Intelligence |
| **Institution** | North-West University |
| **Built by** | [Maluleke Kurhula Success](https://github.com/MALULEKE-KS) |
| **Based in** | South Africa |
| **Core Tech** | Python · BFS · DFS · IDDFS · NetworkX |

---

## Algorithms Implemented

### Breadth-First Search (BFS)
Explores level by level — all neighbors at current
depth before moving deeper. Uses a queue (FIFO).

A Level 0
/
B C Level 1
/ \ /
D E F G Level 2

BFS: A → B → C → D → E → F → G

text

| Property | Value |
| :--- | :--- |
| **Data Structure** | Queue (deque) |
| **Complete** | Yes |
| **Optimal** | Yes (unweighted) |
| **Time** | O(V + E) |
| **Space** | O(V) |

### Depth-First Search (DFS)
Explores deep first — follows each branch
to its end before backtracking. Uses a stack (LIFO).

A
/
B C
/ \ /
D E F G

DFS: A → B → D → E → C → F → G

text

| Property | Value |
| :--- | :--- |
| **Data Structure** | Stack (list) |
| **Complete** | No (without cycle detection) |
| **Optimal** | No |
| **Time** | O(V + E) |
| **Space** | O(V) |

### Iterative Deepening DFS (IDDFS)
Combines DFS memory efficiency with BFS completeness.
Repeated depth-limited searches with increasing limits.

Depth 0: [A]
Depth 1: [A, B, C]
Depth 2: [A, B, D, E, C, F, G]

text

| Property | Value |
| :--- | :--- |
| **Data Structure** | Recursion + Stack |
| **Complete** | Yes |
| **Optimal** | Yes (unweighted) |
| **Time** | O(b^d) |
| **Space** | O(d) |

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/MALULEKE-KS/graph-search-engine.git
cd graph-search-engine

# Install dependencies
pip install networkx matplotlib

# Run the search engine
python src/main.py
Expected Output
text
============================================================
🔍 GRAPH SEARCH ENGINE — Uninformed Search Algorithms
============================================================
Graph: Binary Tree with 7 nodes (A–G)
Root:  A
Depth: 2
============================================================

📊 BFS (Breadth-First Search):
   Visitation Order: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

📊 DFS (Depth-First Search):
   Visitation Order: ['A', 'B', 'D', 'E', 'C', 'F', 'G']

📊 IDDFS (Iterative Deepening DFS):
   Depth 0: ['A']
   Depth 1: ['A', 'B', 'C']
   Depth 2: ['A', 'B', 'D', 'E', 'C', 'F', 'G']

============================================================
✅ Search Complete
============================================================
Project Structure
text
graph-search-engine/
│
├── src/
│   ├── main.py                        # Entry point
│   ├── breadth_first_search.py        # BFS implementation
│   ├── depth_first_search.py          # DFS implementation
│   ├── iterative_deepening_search.py  # IDDFS implementation
│   └── graph_visualizer.py            # NetworkX visualization
│
├── tests/
│   └── .gitkeep
│
├── docs/
│   └── .gitkeep
│
├── output/
│   └── .gitkeep
│
├── .gitignore
├── LICENSE
└── README.md
Algorithm Comparison
Algorithm	Complete	Optimal	Time	Space	Structure
BFS	✅	✅	O(V+E)	O(V)	Queue
DFS	❌	❌	O(V+E)	O(V)	Stack
IDDFS	✅	✅	O(b^d)	O(d)	Recursion
Engineering Philosophy
Principle	Application
Separation of Concerns	Each algorithm in its own module
Type Safety	Full type hints throughout
Error Handling	Input validation with clear messages
Documentation	Docstrings on every function
Visualization	Built-in graph rendering
What I Can Build
Industry	Applications
AI/ML	Search algorithms, game playing, planning
Networking	Network topology traversal
Robotics	Path planning, navigation
Game Development	Map exploration, enemy AI
Web Crawling	Link discovery, site mapping
Social Networks	Connection discovery, friend suggestions
Connect With Me
Portfolio	my-nextjs-portfolio.vercel.app
Email	kurhula04s@gmail.com
WhatsApp	wa.me/27640708649
LinkedIn	linkedin.com/in/kurhula-success-maluleke
GitHub	github.com/MALULEKE-KS
<p align="center"> <em>Built with precision — KSDRILL-SA</em> </p><p align="center"> <img src="https://capsule-render.vercel.app/api?type=wave&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" alt="Footer wave" /> </p> 