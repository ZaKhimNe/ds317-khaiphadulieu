# Hướng dẫn thành viên

Repo có 2 dự án: **`VN1/`** (đang làm) và **`datathon/`** (cũ, chỉ tham khảo). Làm việc với dự án nào thì
chỉ thêm/sửa file trong thư mục của dự án đó.

## 1. Clone repo

```bash
git clone https://github.com/ZaKhimNe/khaipha-dl-doanhnghiep.git
cd khaipha-dl-doanhnghiep
```

## 2. Tải dữ liệu

Dữ liệu không có trên GitHub.

**VN1:** tải 5 file CSV của VN1 Forecasting, đặt vào:

```
VN1/data/raw/vn1-forecasting/
```

(ví dụ phải có `VN1/data/raw/vn1-forecasting/Phase 0 - Sales.csv`). Chi tiết: `VN1/data/README.md`.

**Datathon (nếu cần xem lại):** join competition **Datathon 2026** trên Kaggle, tải 14 file CSV, giải nén vào
`datathon/data/raw/datathon-2026-round-1/`.

## 3. Cài môi trường Python

```bash
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Quy tắc làm việc

- Notebook cá nhân để ở `VN1/notebooks/thanh-vien/<Tên>/`. `VN1/notebooks/eda/` là **bản chuẩn**, chỉ sửa qua PR.
- Code dùng lại nhiều lần đặt trong `VN1/src/vn1/`, notebook chỉ gọi hàm.
- Làm trên nhánh `vn1/<ten>`, mở Pull Request vào `main`, Khiêm review.
- KHÔNG commit file nào trong `*/data/`.
- KHÔNG sửa gì trong `datathon/` (trừ khi được giao). KHÔNG đụng `datathon/notebooks/thanh-vien/Quyen/`.

```bash
git checkout -b vn1/<ten>
# ... làm việc ...
git add VN1/notebooks/thanh-vien/<Tên>/
git commit -m "VN1: <nội dung>"
git push -u origin vn1/<ten>
# rồi mở Pull Request trên GitHub
```

## 5. Kẹt?

Nhắn Khiêm kèm ảnh chụp lỗi.
