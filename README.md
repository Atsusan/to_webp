**コードの動作**

関数 convert_to_webp

**フォルダ作成**

Path(input_folder).mkdir(parents=True, exist_ok=True) で、入力フォルダが存在しない場合は作成。

Path(output_folder).mkdir(parents=True, exist_ok=True) で、出力フォルダが存在しない場合は作成。

**画像の変換処理**

input_folder 内の .jpg, .jpeg, .png ファイルを取得。

Pillow で画像を開き、.webp 形式で output_folder に保存。

変換が完了したら Converted: input_image -> output_image を出力。

**スクリプトのエントリーポイント**

if __name__ == "__main__": でスクリプトを実行したときに動作するようになっている。

input_dir（input_images）にある画像を output_dir（output_webp）へ変換。

**使い方**
input_images フォルダに .jpg, .jpeg, .png の画像を用意する。

スクリプトを実行：
python script.py
output_webp フォルダに .webp 形式の画像が保存される。
