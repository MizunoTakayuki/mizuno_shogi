import os

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


if __name__ == "__main__":
    img_path_list = make_imlist("koma_imgs")
    for i, path in enumerate(img_path_list):
        filename = os.path.basename(path)
        koma_dir = os.path.basename(os.path.dirname(path))
        trip_num = str(i) + "_"
        new_filename = koma_dir.replace(trip_num, '') + str(i) + ".png"
        os.rename(path, os.path.join("koma_imgs", koma_dir, new_filename))

