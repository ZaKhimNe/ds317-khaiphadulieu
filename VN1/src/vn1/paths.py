"""Đường dẫn chuẩn của dự án VN1.

Mặc định đọc dữ liệu từ <repo>/VN1/data/raw/vn1-forecasting.
Chạy ở máy khác / Colab: đặt biến môi trường VN1_DATA_DIR trỏ tới thư mục chứa 5 file CSV.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.environ.get("VN1_DATA_DIR", ROOT / "data" / "raw" / "vn1-forecasting"))
OUTPUT_DIR = Path(os.environ.get("VN1_OUTPUT_DIR", ROOT / "outputs"))


def out_dir(*parts: str) -> Path:
    """Trả về thư mục con trong VN1/outputs/ (tự tạo nếu chưa có)."""
    p = OUTPUT_DIR.joinpath(*parts)
    p.mkdir(parents=True, exist_ok=True)
    return p
