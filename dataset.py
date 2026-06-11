import os
import shutil

def move_files_if_exists(source_dir, target_dir, move_to_dir):

    if not os.path.exists(move_to_dir):
        os.makedirs(move_to_dir)


    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        if os.path.isfile(source_file):
            target_file = os.path.join(target_dir, filename)

            if os.path.isfile(target_file):

                new_location = os.path.join(move_to_dir, filename)
                shutil.move(source_file, new_location)
                print(f"Moved '{filename}' to '{move_to_dir}'")

if __name__ == '__main__':
    # 示例用法
    source_dir = r''
    target_dir = r''
    move_to_dir = r''

    move_files_if_exists(source_dir, target_dir, move_to_dir)