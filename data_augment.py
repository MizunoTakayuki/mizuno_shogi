import os
import cv2


def make_imlist(img_dir):
    # 拡張子の指定
    ext = ".png"
    # 画像pathの配列を宣言
    imlist = []
    # 指定ディレクトリ内を走査(os.walk)
    for cur_dir, dirs, files in os.walk(img_dir):
        for file in files:
            # ファイル名が拡張子(ext)　で終わる時
            if file.endswith(ext):
                # 画像pathを作成
                img_path = os.path.join(cur_dir, file)
                # 画像pathをリストに格納
                imlist.append(img_path)
    return imlist


def create_save_path(img_path, save_dir):
    """元のフォルダ構成を元に保存するpathを作る
    読み込み画像ディレクトリのpath >>> koma_imgs/0_gyoku/gyoku.png
    保存する画像ディレクトリのpath >>> koma_save_imgs/0_gryoku/gyoku.png
    """
    # ファイル名の取得 gyoku.png
    filename = os.path.basename(img_path)
    # ファイルの上のディレクトリの取得O_gyoku
    koma_dir = os.path.basename(os.path.dirname(img_path))
    # 保存するディレクトリのpathを作成
    save_dir_path = os.path.join(save_dir, koma_dir)
    # ディレクトリの作成
    os.makedirs(save_dir_path, exist_ok=True)
    save_path = os.path.join(save_dir_path, filename)
    return save_path


# ↓がメインとなる
if __name__ == "__main__":
    save_dir = "koma_blur_imgs"
    # 平滑化フィルタサイズの宣言
    average_square = (10, 10)
    # 画像pathのリストから画像path を一つ取り出す
    for path in make_imlist("koma_imgs"):
        print(path)
        # 画像の読み込み
        src = cv2.imread(path, 1)
        print("読み込み完了")
        # 画像のぼかし
        blur_img = cv2.blur(src, average_square)
        print("画像をぼかします")
        save_path = create_save_path(img_path=path, save_dir=save_dir)
        cv2.imwrite(save_path, blur_img)
        print("画像の保存完了")
