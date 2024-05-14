import os
import shutil


def copy_dir(root_src_dir: str, root_dst_dir: str) -> None:
    if not os.path.exists(root_src_dir):
        raise ValueError("Error in Source Folder")
    shutil.rmtree(root_dst_dir)
    if not os.path.exists(root_dst_dir):
        os.makedirs(root_dst_dir)
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir: str = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file in files:
            src_file: str = os.path.join(src_dir, file)
            dst_file: str = os.path.join(dst_dir, file)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            print(f"copying {src_file} to {dst_file}")
            print()
            shutil.copy(src_file, dst_dir)
