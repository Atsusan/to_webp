from pathlib import Path
from PIL import Image

def convert_to_webp(input_folder: str, output_folder: str, quality: int = 80):
    input_path = Path(input_folder)
    input_path.mkdir(parents=True, exist_ok=True)  # 入力フォルダがなければ作成
    
    """
    指定されたフォルダ内のJPEG/PNG画像をWebP形式に変換し、圧縮する。
    
    :param input_folder: 入力フォルダのパス
    :param output_folder: 出力フォルダのパス
    :param quality: WebPの品質（1-100）
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for image_file in input_path.glob("*.*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            with Image.open(image_file) as img:
                webp_file = output_path / f"{image_file.stem}.webp"
                img.save(webp_file, "WEBP", quality=quality)
                print(f"Converted: {image_file} -> {webp_file}")

if __name__ == "__main__":
    input_dir = "input_images"  # 変換したい画像があるフォルダ
    output_dir = "output_webp"   # 出力フォルダ
    convert_to_webp(input_dir, output_dir, quality=80)