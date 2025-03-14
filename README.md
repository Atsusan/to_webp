1. Python のインストール
まず、Python がインストールされているか確認してください。

python --version
もし Python がインストールされていなければ、公式サイトからダウンロードしてインストールしてください。

2. 必要なライブラリのインストール
このスクリプトでは、以下のライブラリを使用します。

✅ pathlib（標準ライブラリなのでインストール不要）
✅ Pillow（画像処理ライブラリ）

Pillow は pip を使ってインストールできます。

pip install Pillow
または、requirements.txt を作成して以下の内容を記述し、

Pillow

次のコマンドで一括インストールすることもできます。

pip install -r requirements.txt

3. フォルダの準備

スクリプトを実行する前に、画像を格納するフォルダを作成してください。

mkdir input_images

このフォルダに .jpg, .jpeg, .png の画像を入れておきます。

4. スクリプトの実行
   
準備が整ったら、Python スクリプトを実行します。

python webp.py

変換が成功すると、output_webp フォルダに WebP 形式の画像が出力されます。

動作確認

変換された画像を確認したい場合は、Mac のプレビューや Chrome で開いてみてください。

Macの場合

open output_webp/sample.webp

Linuxの場合

xdg-open output_webp/sample.webp

Windowsの場合 画像をダブルクリックで開くか、Chrome にドラッグ＆ドロップしてください。




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
python webp.py
output_webp フォルダに .webp 形式の画像が保存される。
