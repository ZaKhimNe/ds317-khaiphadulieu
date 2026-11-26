# VN1 Forecasting – dự báo doanh số tuần

Dữ liệu VN1 Forecasting: doanh số (số lượng bán) và giá theo **tuần × (Client, Warehouse, Product)**.

## Dữ liệu (`data/raw/vn1-forecasting/`)

| File | Nội dung | Số chuỗi | Tuần | Khoảng thời gian |
|---|---|---|---|---|
| `Phase 0 - Sales.csv` | số lượng bán | 15 053 | 170 | 2020-07-06 → 2023-10-02 |
| `Phase 0 - Price.csv` | giá bán TB tuần (trống = không bán) | 15 053 | 170 | 2020-07-06 → 2023-10-02 |
| `Phase 1 - Sales.csv` | số lượng bán | 15 053 | 13 | 2023-10-09 → 2024-01-01 |
| `Phase 1 - Price.csv` | giá bán | 15 053 | 13 | 2023-10-09 → 2024-01-01 |
| `Phase 2 - Sales.csv` | số lượng bán (không có giá) | 15 053 | 13 | 2024-01-08 → 2024-04-01 |

- Dạng **wide**: 3 cột khoá `Client, Warehouse, Product` + mỗi cột là 1 tuần, tên cột = ngày Thứ Hai đầu tuần.
- Phase 0 + 1 là lịch sử để huấn luyện; Phase 2 là 13 tuần cần dự báo (đáp án).
- `vn1-forecasting.zip` là file tải gốc (cùng nội dung 5 CSV).

## Cấu trúc

```
data/raw/vn1-forecasting/   CSV gốc (không chỉnh sửa, không lên GitHub)
src/vn1/                    thư viện dùng chung – paths.py: ROOT, DATA_DIR, OUTPUT_DIR, out_dir()
notebooks/01_DS317.R11_DeXuat_Code_VN1.ipynb   notebook cho Bản đề xuất
notebooks/eda/              notebook EDA chuẩn
notebooks/thanh-vien/<Tên>/ notebook cá nhân
outputs/                    ảnh, bảng, submission do notebook sinh ra
huy-forecasting/            pipeline đầy đủ của Huy (copy từ github.com/huyml-911/DS317-VN1-forecasting)
```

### `huy-forecasting/`

Làm sạch → EDA → phân nhóm kiểu nhu cầu (Syntetos-Boylan) → chất lượng dữ liệu → dự báo (gradient boosting trộn với
phương pháp đơn giản theo từng nhóm) → đánh giá → phân tích sai số. Điểm VN1 (doanh thu, TB 4 kỳ 2023): **55,6**
so với naive 65,4. Code ở `scripts/01…09`, hình và số liệu ở `reports/`, đọc data từ `data/raw/vn1-forecasting/`
ở trên. Cách chạy: [huy-forecasting/README.md](huy-forecasting/README.md).

## Dùng thư viện trong notebook

```python
import sys
from pathlib import Path
ROOT = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "src" / "vn1").is_dir())
sys.path.insert(0, str(ROOT / "src"))

from vn1.paths import DATA_DIR, out_dir
```

Chạy trên Colab/máy khác: đặt biến môi trường `VN1_DATA_DIR` trỏ tới thư mục chứa 5 file CSV.
