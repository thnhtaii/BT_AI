import json

code = """import time
from collections import deque

def in_mt(mt):
    res = ""
    for i in range(3):
        row = ""
        for j in range(3):
            val = mt[i*3 + j]
            if val == 0:
                row += " [ ] "
            else:
                row += f"  {val}  "
        res += row + "\\n"
    res += "-" * 20 + "\\n"
    return res

def get_successors(mt):
    pos = mt.index(0)
    r, c = pos // 3, pos % 3
    successors = []
    
    def swap(mt, i, j):
        new_mt = list(mt)
        new_mt[i], new_mt[j] = new_mt[j], new_mt[i]
        return new_mt
        
    if r > 0: successors.append(("Lên", swap(mt, pos, pos - 3)))
    if r < 2: successors.append(("Xuống", swap(mt, pos, pos + 3)))
    if c > 0: successors.append(("Trái", swap(mt, pos, pos - 1)))
    if c < 2: successors.append(("Phải", swap(mt, pos, pos + 1)))
    return successors

def bfs(start_state, goal_state, mode="early"):
    if start_state == goal_state:
        return [], 0
        
    frontier = deque([(start_state, [])])
    
    if mode == "early":
        explored = set([tuple(start_state)])
    else:
        explored = set()
        
    nodes_generated = 1
    
    while frontier:
        node, path = frontier.popleft()
        
        if mode == "late" and node == goal_state:
            return path, nodes_generated
            
        if mode == "late":
            if tuple(node) in explored:
                continue
            explored.add(tuple(node))
            
        for action, child in get_successors(node):
            if mode == "early":
                nodes_generated += 1
                if child == goal_state:
                    return path + [(action, child)], nodes_generated
                if tuple(child) not in explored:
                    explored.add(tuple(child))
                    frontier.append((child, path + [(action, child)]))
            else:
                if tuple(child) not in explored:
                    frontier.append((child, path + [(action, child)]))
                    nodes_generated += 1
                    
    return None, nodes_generated

# ==========================================
# GIAO DIỆN SIÊU NHẸ (Chỉ dùng Text / Code)
# ==========================================

print("=== BỘ GIẢI 8-PUZZLE SIÊU NHẸ ===")
print("Bạn có muốn nhập ma trận bằng tay không? (y/n)")
choice = input("Lựa chọn (y/n, mặc định là n để dùng mảng có sẵn): ").strip().lower()

start_state = []
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

if choice == 'y':
    print("\\nNhập từng hàng (mỗi số cách nhau bằng dấu cách, dùng số 0 cho ô trống):")
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Hàng {i+1}: ").split()))
                if len(row) == 3 and all(0 <= x <= 8 for x in row):
                    start_state.extend(row)
                    break
                else:
                    print("Lỗi: Vui lòng nhập đúng 3 số từ 0 đến 8!")
            except ValueError:
                print("Lỗi: Vui lòng chỉ nhập số!")
else:
    # Cấu hình trực tiếp trong code (Cách nhẹ nhất, 0 tốn RAM giao diện)
    start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    print("\\nĐang sử dụng ma trận mặc định...")

print("\\nTrạng thái bắt đầu:")
print(in_mt(start_state))

print("Chọn cơ chế tìm kiếm:")
print("1. Early Goal Test (Tìm nhanh)")
print("2. Late Goal Test (Tìm chậm hơn)")
mode_choice = input("Nhập số (1 hoặc 2): ").strip()

mode = "late" if mode_choice == "2" else "early"
print(f"\\nĐang giải bằng BFS - Cơ chế {mode.upper()} Goal Test...")

start_time = time.time()
path, nodes_generated = bfs(start_state, goal_state, mode)
end_time = time.time()

if path is not None:
    print(f"\\n>>> THÀNH CÔNG! <<<")
    print(f"Số bước (độ sâu): {len(path)}")
    print(f"Số trạng thái đã sinh: {nodes_generated}")
    print(f"Thời gian giải: {end_time - start_time:.4f} giây")
    
    xem = input("\\nBạn có muốn xem chi tiết từng bước đi không? (y/n): ").strip().lower()
    if xem == 'y':
        for step, (action, state) in enumerate(path):
            print(f"Bước {step + 1}: Di chuyển ô trống sang {action}")
            print(in_mt(state))
else:
    print("Không tìm thấy giải pháp!")
"""

lines = [line + '\\n' for line in code.split('\\n')]
if lines and lines[-1] == '\\n':
    lines.pop()
elif lines and lines[-1].endswith('\\n'):
    lines[-1] = lines[-1][:-1]

nb = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Giải mã 8-Puzzle - Phiên bản Siêu Nhẹ (Minimalist)\\n",
                "Phiên bản này **loại bỏ hoàn toàn các thư viện đồ họa (như ipywidgets)** để đạt tốc độ xử lý nhanh nhất và tiêu tốn ít RAM nhất. \\n",
                "Bạn sẽ tương tác bằng cách gõ phím trực tiếp vào bảng console (hoặc sửa biến số trong ô mã)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": lines
        }
    ]
}

with open(r'd:\ky 2 nam 2\AI\bfs\8puzzle_minimal.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
