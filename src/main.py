import os
import shutil

from utils import copy_dir, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:

    print("Deleting Public Folder")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_dir(dir_path_static, dir_path_public)
    print("Generating Content")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )


if __name__ == "__main__":
    main()
