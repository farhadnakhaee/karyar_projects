import os
import sys
import time


def sort_img_and_vid(src, dst):
    ttype_image = ['jpg', 'jpeg', 'png']
    ttype_video = ['mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov']

    for file_dir in os.walk(src):
        for file_name in file_dir[2]:

            if '.' in file_name and file_name.split(".")[-1].lower() in ttype_image:
                src_file_dir, dst_file_dir = make_dir(dst, 'Images', file_dir[0], file_name)
                copy(src_file_dir, dst_file_dir)

            elif '.' in file_name and file_name.split(".")[-1].lower() in ttype_video:
                src_file_dir, dst_file_dir = make_dir(dst, 'Videos', file_dir[0], file_name)
                copy(src_file_dir, dst_file_dir)


def make_dir(dst, file_type, file_dir, file_name):
    src_file_dir = os.path.join(file_dir, file_name)
    year = time.ctime(os.path.getmtime(src_file_dir)).split()[-1]
    if not os.path.exists(dst):
        os.mkdir(dst)
    if not os.path.isdir(f"{dst}/{year}"):
        os.mkdir(f"{dst}/{year}")
    if not os.path.isdir(f"{dst}/{year}/{file_type}"):
        os.mkdir(f"{dst}/{year}/{file_type}")

    dst_file_dir = os.path.join(dst, year, file_type, file_name)

    return src_file_dir, dst_file_dir


def copy(src_file_dir, dst_file_dir):
    with open(src_file_dir, 'rb') as src_file:
        file_content = src_file.read()

    with open(dst_file_dir, 'wb') as dst_file:
        dst_file.write(file_content)


if __name__ == '__main__':
    source_path = sys.argv[1]
    destination_path = sys.argv[2]
    sort_img_and_vid(source_path, destination_path)
