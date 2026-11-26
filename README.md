# DS317.R11 – Khai phá dữ liệu trong doanh nghiệp (nhóm 8)

Repo chia làm **2 dự án độc lập**, mỗi dự án có data, code, notebook, output riêng. Không dùng chéo file giữa hai bên.

| Thư mục | Bộ dữ liệu | Trạng thái |
|---|---|---|
| [`VN1/`](VN1/README.md) | VN1 Forecasting – doanh số tuần theo Client × Warehouse × Product (2020-07 → 2024-04) | **Đang làm** |
| [`datathon/`](datathon/README.md) | Datathon 2026 Round 1 – TMĐT thời trang, dự báo doanh thu tuần × danh mục | Tạm dừng (giữ để tham khảo) |

## Cấu trúc

```
VN1/                 Dự án mới (xem VN1/README.md)
  data/raw/          CSV gốc – không lên GitHub
  src/vn1/           thư viện dùng chung của VN1
  notebooks/         eda/ và thanh-vien/<Tên>/
  outputs/
datathon/            Dự án cũ, giữ nguyên cấu trúc bên trong (data, src/ds317, notebooks, outputs, scripts, archive, docs)
docs/                Tài liệu chung của nhóm: hướng dẫn thành viên, phân công, tài liệu môn học
requirements.txt     Môi trường Python dùng chung cho cả hai dự án
```

**Thành viên:** đọc [docs/HUONG-DAN-THANH-VIEN.md](docs/HUONG-DAN-THANH-VIEN.md).

## Cài đặt

```bash
py -3 -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Notebook của mỗi dự án tự dò ngược lên thư mục chứa `data/raw` (hoặc `src/<thư viện>`) nên luôn đọc đúng data của
dự án mình, chạy từ đâu cũng được.
