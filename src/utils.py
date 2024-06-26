import os
import shutil
from pathlib import Path
from typing import Any

from htmlnode import ParentNode
from markdown_blocks import extract_title, markdown_to_html_node


def copy_dir(root_src_dir: str, root_dst_dir: str) -> None:
    if not os.path.exists(root_src_dir):
        raise ValueError("Error in Source Folder")
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


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file: Any = open(from_path, "r")
    markdown_content: str = markdown_file.read()
    markdown_file.close()
    template_file: Any = open(template_path, "r")
    template_content: str = template_file.read()
    template_file.close()
    html_node: ParentNode = markdown_to_html_node(markdown_content)
    html: str = html_node.to_html()
    title: str = extract_title(markdown_content)
    to_write: str = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html
    )
    folder: str = os.path.dirname(dest_path)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    file: Any = open(dest_path, "w")
    file.write(to_write)
    file.close()


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
) -> None:
    if not os.path.exists(dir_path_content):
        raise ValueError("Error in Source Folder")
    for src_dir, dirs, files in os.walk(dir_path_content):
        for file in files:
            file_name: str = os.path.join(src_dir, file)
            if Path(file_name).suffix == ".md":
                dir: str = src_dir.removeprefix(dir_path_content).lstrip("/")
                dest_path: str = os.path.join(
                    dest_dir_path, dir, file.removesuffix(".md") + ".html"
                )
                generate_page(
                    file_name,
                    template_path,
                    dest_path,
                )
