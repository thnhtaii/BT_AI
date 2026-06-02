# Hướng dẫn sử dụng bộ giải 8-Puzzle bằng BFS

Thư mục này chứa 2 phiên bản giải bài toán 8-Puzzle bằng thuật toán **Breadth-First Search (BFS)** với hai cơ chế kiểm tra trạng thái đích khác nhau. Các chương trình được thiết kế chạy trên môi trường Jupyter Notebook và có giao diện nút bấm trực quan để tương tác.

## 📁 Cấu trúc tệp tin

1. **`8puzzle_late_goal.ipynb`**: 
   - Sử dụng cơ chế **Late Goal Test** (Xét mục tiêu muộn).
   - *Cách hoạt động*: Thuật toán sẽ lấy một trạng thái ra khỏi hàng đợi (queue) rồi mới kiểm tra xem đó có phải là trạng thái đích hay không. Cơ chế này đảm bảo tìm được đường đi ngắn nhất (trong một số biến thể thuật toán) nhưng có thể sẽ sinh ra và xét nhiều trạng thái hơn.

2. **`8puzzle_early_goal.ipynb`**:
   - Sử dụng cơ chế **Early Goal Test** (Xét mục tiêu sớm).
   - *Cách hoạt động*: Ngay khi một trạng thái mới vừa được sinh ra từ hàm kế thừa, thuật toán lập tức kiểm tra xem nó có phải đích không. Nếu đúng, nó dừng lại ngay. Nhờ vậy, cơ chế này thường cho kết quả nhanh hơn và sinh ra ít trạng thái (node) thừa hơn so với Late Goal.

---

## 🛠️ Yêu cầu hệ thống (Prerequisites)

Để có thể chạy và hiển thị giao diện các tệp tin này, bạn cần cài đặt:
- Python 3.x
- Thư viện `ipywidgets` (Dùng để tạo ô nhập liệu và nút bấm giao diện). 
  *(Lưu ý: Nếu bạn dùng Trợ lý AI để yêu cầu cài, thư viện này có thể đã được cài sẵn cho bạn rồi).*
- Môi trường chạy Jupyter: Bạn có thể dùng trực tiếp **VSCode** (cài extension *Jupyter*) hoặc mở bằng **Jupyter Notebook / JupyterLab** trên trình duyệt.

---

## 🚀 Hướng dẫn cách chạy (How to use)

### Bước 1: Mở tệp tin
Mở một trong hai tệp `8puzzle_late_goal.ipynb` hoặc `8puzzle_early_goal.ipynb` bằng phần mềm hỗ trợ (ví dụ: Visual Studio Code).

### Bước 2: Khởi chạy mã nguồn
Bấm nút **Run All** (hoặc chạy từng ô mã - Cell) để nạp thư viện và hàm thuật toán.
Sau khi chạy thành công ô mã cuối cùng, một giao diện đồ họa nhỏ sẽ hiện ra ngay bên dưới.

### Bước 3: Tương tác với giao diện
1. **Nhập ma trận 8-puzzle**: 
   Giao diện hiển thị một lưới 3x3 gồm 9 ô nhập liệu. Hãy nhập các con số từ `1` đến `8`, và số `0` sẽ đại diện cho **ô trống** (ô có thể di chuyển). 
   *Ví dụ một trạng thái hợp lệ:*
   ```text
   2  8  3
   1  6  4
   7  0  5
   ```
2. **Nhấn nút "Giải"**:
   Nhấn vào nút màu xanh lá (có ghi *Giải (Late/Early Goal Test)*).
3. **Xem kết quả**: 
   Chương trình sẽ tính toán và in kết quả ra ngay bên dưới nút bấm. Thông tin bao gồm:
   - Số bước (độ sâu) để hoàn thành.
   - Số trạng thái (node) đã được thuật toán sinh ra trong quá trình chạy.
   - Thời gian giải bài toán (tính bằng giây).
   - Chi tiết từng bước đi của ô trống (Lên, Xuống, Trái, Phải) kèm theo ma trận trực quan sau mỗi bước.

---

## 💡 Mẹo nhỏ (Tips)
- Hãy thử nhập cùng một ma trận trạng thái ban đầu ở cả hai tệp tin để **so sánh sự khác biệt** về *Số trạng thái đã sinh* và *Thời gian giải* giữa cơ chế kiểm tra mục tiêu sớm (Early) và muộn (Late).
- **Lưu ý**: BFS có thể tốn khá nhiều thời gian và bộ nhớ đối với các trạng thái ban đầu nằm quá xa trạng thái đích (cần quá nhiều số bước đi). Trạng thái đích được mặc định trong code là:
  ```text
  1  2  3
  4  5  6
  7  8  0
  ```
