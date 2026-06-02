import random
import time
from collections import deque
import threading
import ipywidgets as widgets
from IPython.display import display, clear_output

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
        res += row + "\n"
    res += "-" * 20 + "\n"
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
    explored = set()
    
    if mode == "early":
        explored.add(tuple(start_state))
        
    nodes_generated = 1
    
    while frontier:
        node, path = frontier.popleft()
        
        if mode == "late":
            if tuple(node) in explored:
                continue
            explored.add(tuple(node))
            if node == goal_state:
                return path, nodes_generated
                
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

# --- UI Components ---

input_boxes = [widgets.BoundedIntText(value=v, min=0, max=8, layout=widgets.Layout(width='50px', height='50px')) 
               for v in [2, 8, 3, 1, 6, 4, 7, 0, 5]]
input_grid = widgets.GridBox(input_boxes, layout=widgets.Layout(grid_template_columns="repeat(3, 60px)"))

btn_early = widgets.Button(description="Giải (Early Goal Test)", button_style='success', layout=widgets.Layout(width='180px'))
btn_late = widgets.Button(description="Giải (Late Goal Test)", button_style='info', layout=widgets.Layout(width='180px'))
btns_box = widgets.HBox([btn_early, btn_late])

out_text = widgets.Output(layout=widgets.Layout(max_height='400px', overflow='auto', border='1px solid #ccc', padding='10px'))
anim_html = widgets.HTML(value="")

def render_board(state):
    html_content = '''
    <div style="display: grid; grid-template-columns: repeat(3, 80px); gap: 5px; background-color: #5c3a21; padding: 10px; width: fit-content; border-radius: 8px; box-shadow: 3px 3px 15px rgba(0,0,0,0.6); border: 4px solid #3e2412;">
    '''
    for val in state:
        if val == 0:
            html_content += '<div style="width: 80px; height: 80px; background-color: rgba(0,0,0,0.3); border-radius: 4px; box-shadow: inset 2px 2px 5px rgba(0,0,0,0.5);"></div>'
        else:
            html_content += f'''
            <div style="width: 80px; height: 80px; background-color: #e5c088; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 45px; font-weight: bold; color: #3b2210; box-shadow: inset 2px 2px 4px rgba(255,255,255,0.6), inset -2px -2px 4px rgba(0,0,0,0.4), 2px 2px 4px rgba(0,0,0,0.3); font-family: serif; text-shadow: 1px 1px 0px rgba(255,255,255,0.4);">
                {val}
            </div>
            '''
    html_content += '</div>'
    anim_html.value = html_content

def animate_path(start_state, path):
    render_board(start_state)
    time.sleep(1)
    for action, state in path:
        render_board(state)
        time.sleep(0.6)

def solve_and_animate(mode):
    out_text.clear_output()
    start_state = [box.value for box in input_boxes]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    
    render_board(start_state)
    
    with out_text:
        if sorted(start_state) != list(range(9)):
            print("Lỗi: Ma trận phải chứa đầy đủ các số từ 0 đến 8 và không được trùng lặp!")
            return

        print(f"ĐANG GIẢI BẰNG CƠ CHẾ: {mode.upper()} GOAL TEST")
        print("-" * 30)
        start_time = time.time()
        
        path, nodes_generated = bfs(start_state, goal_state, mode)
        
        end_time = time.time()
        if path is not None:
            print(f"Thành công! Số bước đi: {len(path)}")
            print(f"Số trạng thái đã sinh: {nodes_generated}")
            print(f"Thời gian thuật toán chạy: {end_time - start_time:.4f} giây")
            print("\nBắt đầu chạy mô phỏng đồ họa...")
            print("\n=== LOG CHI TIẾT CÁC BƯỚC ===")
            print("Trạng thái bắt đầu:")
            print(in_mt(start_state))
            for step, (action, state) in enumerate(path):
                print(f"Bước {step + 1}: Di chuyển ô trống sang {action}")
                print(in_mt(state))
                
            thread = threading.Thread(target=animate_path, args=(start_state, path))
            thread.start()
            
        else:
            print("Không tìm thấy giải pháp (hoặc trạng thái không thể giải được)!")

btn_early.on_click(lambda b: solve_and_animate("early"))
btn_late.on_click(lambda b: solve_and_animate("late"))

main_ui = widgets.VBox([
    widgets.Label("1. Nhập ma trận 8-Puzzle (0 là ô trống):", style={'font_weight': 'bold'}), 
    input_grid, 
    widgets.HTML("<br>"),
    widgets.Label("2. Chọn thuật toán để bắt đầu giải và xem mô phỏng:", style={'font_weight': 'bold'}),
    btns_box, 
    widgets.HTML("<hr style='border: 1px solid #ccc; width: 100%;'>"),
    widgets.HBox([
        widgets.VBox([
            widgets.Label("Hiệu ứng mô phỏng:", style={'font_weight': 'bold', 'font_size': '16px'}), 
            widgets.HTML("<br>"),
            anim_html
        ], layout=widgets.Layout(margin='0 40px 0 0')),
        
        widgets.VBox([
            widgets.Label("Log Text quá trình chạy:", style={'font_weight': 'bold', 'font_size': '16px'}), 
            out_text
        ], layout=widgets.Layout(width='100%'))
    ], layout=widgets.Layout(width='100%'))
])

render_board([2, 8, 3, 1, 6, 4, 7, 0, 5])
display(main_ui)