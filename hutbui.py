def in_mt(mt, r_robot, c_robot):
    for i in range(3):
        dong = ""
        for j in range(3):
            gia_tri = mt[i * 3 + j]
            if i == r_robot and j == c_robot:
                dong += f"[{gia_tri}] "
            else:
                dong += f" {gia_tri}  "
        print(dong)
    print('---')

def nhap_mt(ten):
    print(f'Nhập trạng thái sàn nhà {ten} (0: Sạch, 1: Bẩn) ')
    mt = []
    for i in range(3):
        while True:
            hang = input(f'Nhập hàng {i+1}: ').split()
            if len(hang) == 3:
                for so in hang:
                    mt.append(int(so))
                break
            else:
                print('Nhập đúng 3 số (0 hoặc 1)')
    return mt

def giai_toan():
    trang_thai_dau = nhap_mt("BAN ĐẦU")
    print("Nhập vị trí ban đầu của máy hút bụi:")
    r_dau = int(input("Nhập hàng (1-3): ")) - 1
    c_dau = int(input("Nhập cột (1-3): ")) - 1
    
    lich_su = [{'bc': trang_thai_dau, 'r': r_dau, 'c': c_dau, 'cha': -1, 'hd': 'Bắt đầu'}]
    danh_sach_cho = [0]
    da_tung_qua = [(tuple(trang_thai_dau), r_dau, c_dau)]

    while danh_sach_cho:
        chi_so_hien_tai = danh_sach_cho.pop(0)
        nut_hien_tai = lich_su[chi_so_hien_tai]

        if sum(nut_hien_tai['bc']) == 0:
            print("\nChuỗi hành động là: ")
            duong_di = []
            while chi_so_hien_tai != -1:
                duong_di.append(lich_su[chi_so_hien_tai])
                chi_so_hien_tai = lich_su[chi_so_hien_tai]['cha']
            
            for buoc, nut in enumerate(reversed(duong_di)):
                print(f"{buoc}: {nut['hd']}")
                in_mt(nut['bc'], nut['r'], nut['c'])
            return

        r, c = nut_hien_tai['r'], nut_hien_tai['c']
        vi_tri_phang = r * 3 + c

        # Luật: Hút bụi
        if nut_hien_tai['bc'][vi_tri_phang] == 1:
            bc_moi = list(nut_hien_tai['bc'])
            bc_moi[vi_tri_phang] = 0
            if (tuple(bc_moi), r, c) not in da_tung_qua:
                da_tung_qua.append((tuple(bc_moi), r, c))
                lich_su.append({'bc': bc_moi, 'r': r, 'c': c, 'cha': chi_so_hien_tai, 'hd': 'Hút bụi'})
                danh_sach_cho.append(len(lich_su) - 1)

        # Luật: Lên
        if r > 0:
            if (tuple(nut_hien_tai['bc']), r - 1, c) not in da_tung_qua:
                da_tung_qua.append((tuple(nut_hien_tai['bc']), r - 1, c))
                lich_su.append({'bc': nut_hien_tai['bc'], 'r': r - 1, 'c': c, 'cha': chi_so_hien_tai, 'hd': 'Lên'})
                danh_sach_cho.append(len(lich_su) - 1)

        # Luật: Xuống
        if r < 2:
            if (tuple(nut_hien_tai['bc']), r + 1, c) not in da_tung_qua:
                da_tung_qua.append((tuple(nut_hien_tai['bc']), r + 1, c))
                lich_su.append({'bc': nut_hien_tai['bc'], 'r': r + 1, 'c': c, 'cha': chi_so_hien_tai, 'hd': 'Xuống'})
                danh_sach_cho.append(len(lich_su) - 1)

        # Luật: Sang trái
        if c > 0:
            if (tuple(nut_hien_tai['bc']), r, c - 1) not in da_tung_qua:
                da_tung_qua.append((tuple(nut_hien_tai['bc']), r, c - 1))
                lich_su.append({'bc': nut_hien_tai['bc'], 'r': r, 'c': c - 1, 'cha': chi_so_hien_tai, 'hd': 'Trái'})
                danh_sach_cho.append(len(lich_su) - 1)

        # Luật: Sang phải
        if c < 2:
            if (tuple(nut_hien_tai['bc']), r, c + 1) not in da_tung_qua:
                da_tung_qua.append((tuple(nut_hien_tai['bc']), r, c + 1))
                lich_su.append({'bc': nut_hien_tai['bc'], 'r': r, 'c': c + 1, 'cha': chi_so_hien_tai, 'hd': 'Phải'})
                danh_sach_cho.append(len(lich_su) - 1)

    print("Không tìm thấy đường đi!")

if __name__ == "__main__":
    giai_toan()