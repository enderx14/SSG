import os
import shutil

from utils import copy_dir, generate_page


def main() -> None:
    root_src_dir = "/home/ender/Projects/BootDev/SSG/static"
    root_dst_dir = "/home/ender/Projects/BootDev/SSG/public"
    print("Deleting Public Folder")
    if os.path.exists(root_dst_dir):
        shutil.rmtree(root_dst_dir)

    print("Copying static files to public directory...")
    copy_dir(root_src_dir, root_dst_dir)
    generate_page("./content/index.md", "template.html", "./public/index.html")


if __name__ == "__main__":
    main()
