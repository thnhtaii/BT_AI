# 🧩 BT_AI - Bài Tập Trí Tuệ Nhân Tạo

Nơi lưu trữ các bài thực hành và bài tập trên lớp môn **Trí Tuệ Nhân Tạo** — tập trung vào bài toán **8-Puzzle** với nhiều thuật toán tìm kiếm khác nhau.

## 📖 Mô tả

Dự án triển khai và so sánh **10 thuật toán tìm kiếm** áp dụng cho bài toán 8-Puzzle, bao gồm cả thuật toán tìm kiếm không có thông tin (Uninformed Search) và có thông tin (Informed Search). Mỗi thuật toán đều có:

- **File thuật toán** (`.ipynb`): Chứa logic thuật toán
- **File giao diện** (`ui*.ipynb`): Giao diện trực quan với animation, log chi tiết từng bước

## 🗂️ Cấu trúc thư mục

```
AI/
│
├── 📁 Uninformed_Search/ (Tìm kiếm không có thông tin)
│   ├── bfs/                          # Breadth-First Search
│   ├── dfs/                          # Depth-First Search
│   └── ucs/                          # Uniform Cost Search
│
├── 📁 Informed_Search/ (Tìm kiếm có thông tin)
│   ├── Greedy Best-First Search/     # Tìm kiếm tham lam tốt nhất
│   ├── A star/                       # Thuật toán A*
│   └── IDA/                          # Iterative Deepening A*
│
├── 📁 Local_Search/ (Tìm kiếm cục bộ)
│   ├── Simple_Hill_Climbing/         # Leo đồi đơn giản
│   ├── Hill_Climbing/                # Leo đồi dốc nhất (Steepest-Ascent)
│   ├── Stochastic__Hill_Climbing/    # Leo đồi ngẫu nhiên
│   ├── Random_restart_Hill_Climbing/ # Leo đồi khởi động lại ngẫu nhiên
│   └── Local_Beam_Search/            # Tìm kiếm chùm cục bộ
│
├── 📄 8puzzle.ipynb                  # Bài toán 8-puzzle cơ bản
├── 📄 hutbui.ipynb                   # Bài toán hút bụi
├── 📄 hutbuimodel.ipynb              # Mô hình hút bụi
├── 📄 hutbuitrenlop.ipynb            # Bài tập hút bụi trên lớp
└── 📄 README.md
```

## 🔍 Chi tiết các thuật toán

### 1. Tìm kiếm không có thông tin (Uninformed Search)

| Thuật toán | Thư mục | Mô tả |
|:-----------|:--------|:------|
| **BFS** | `Uninformed_Search/bfs/` | Duyệt theo chiều rộng, đảm bảo tìm lời giải ngắn nhất |
| **DFS** | `Uninformed_Search/dfs/` | Duyệt theo chiều sâu, tiết kiệm bộ nhớ |
| **UCS** | `Uninformed_Search/ucs/` | Tìm kiếm chi phí đồng nhất, mở rộng nút có chi phí thấp nhất |

### 2. Tìm kiếm có thông tin (Informed Search)

| Thuật toán | Thư mục | Heuristic | Mô tả |
|:-----------|:--------|:----------|:------|
| **Greedy Best-First** | `Informed_Search/Greedy Best-First Search/` | Manhattan | Chọn nút có h(n) nhỏ nhất |
| **A*** | `Informed_Search/A star/` | Manhattan + Cost | f(n) = g(n) + h(n), đảm bảo tối ưu |
| **IDA*** | `Informed_Search/IDA/` | Manhattan + Misplaced | A* với giới hạn độ sâu lặp |

### 3. Tìm kiếm cục bộ (Local Search)

| Thuật toán | Thư mục | Heuristic | Mô tả |
|:-----------|:--------|:----------|:------|
| **Simple Hill Climbing** | `Local_Search/Simple_Hill_Climbing/` | Manhattan / Misplaced | Chọn nút con đầu tiên tốt hơn |
| **Steepest-Ascent HC** | `Local_Search/Hill_Climbing/` | Manhattan / Misplaced | Chọn nút con tốt nhất trong tất cả |
| **Stochastic HC** | `Local_Search/Stochastic__Hill_Climbing/` | Manhattan / Misplaced | Chọn ngẫu nhiên từ các nút tốt hơn |
| **Random Restart HC** | `Local_Search/Random_restart_Hill_Climbing/` | Manhattan | Restart ngẫu nhiên khi bị kẹt |
| **Local Beam Search** | `Local_Search/Local_Beam_Search/` | Manhattan | Duy trì k trạng thái tốt nhất song song |

## 🎯 Bài toán 8-Puzzle

### Ví dụ

```
Trạng thái bắt đầu:        Trạng thái đích:
  2  8  3                     1  2  3
  1  6  4                     8  [ ]  4
  7  [ ]  5                   7  6  5
```

### Heuristic sử dụng

- **Số ô sai vị trí (Misplaced Tiles)**: Đếm số ô không đúng vị trí so với trạng thái đích
- **Khoảng cách Manhattan**: Tổng khoảng cách Manhattan của từng ô đến vị trí đích

## 🚀 Cách chạy

### Yêu cầu

- Python 3.x
- Jupyter Notebook
- Các thư viện: `ipywidgets`, `IPython`

### Hướng dẫn

1. Mở Jupyter Notebook
2. Vào thư mục thuật toán muốn chạy
3. Mở file `ui*.ipynb` (file giao diện)
4. Chạy tất cả các cell (`Run All`)
5. Tương tác với giao diện: nhập trạng thái, chọn heuristic, nhấn nút tìm kiếm

```bash
# Cài đặt thư viện cần thiết
pip install jupyter ipywidgets

# Chạy Jupyter Notebook
jupyter notebook
```

## 🖥️ Giao diện

Mỗi thuật toán đều có giao diện trực quan bao gồm:

- **🎮 Input Grid**: Nhập trạng thái bắt đầu (có nút Random, Reset, Load Example)
- **📊 Statistics**: Hiển thị số bước, số nút sinh ra, thời gian, trạng thái
- **🎬 Visual Simulation**: Animation mô phỏng quá trình giải
- **📋 Execution Log**: Log chi tiết từng bước thuật toán

## 👤 Tác giả

Sinh viên thực hiện bài tập môn Trí Tuệ Nhân Tạo.
