import argparse
import os

def get_folder_size(folder_path):
    size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size/1024

def get_file_size(file_path):
    return os.path.getsize(file_path)/1024

def main():
    parser = argparse.ArgumentParser(description='Calculate size of file/folder')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--directory', type=str, help='the directory to calculate size for')
    group.add_argument('-f', '--file', type=str, help='the file to calculate size for')
    parser.add_argument('-F', '--filetype', type=str, help='the file type to filter')
    args = parser.parse_args()

    if args.directory:
        if args.filetype:
            total_size = 0
            for root, dirs, files in os.walk(args.directory):
                for file in files:
                    if file.endswith(args.filetype):
                        total_size += os.path.getsize(os.path.join(root, file))
            print(f"Total size of {args.filetype} files: {total_size/1024} KB")
        else:
            print(f"Size of directory {args.directory}: {get_folder_size(args.directory)} KB")
    elif args.file:
        print(f"Size of file {args.file}: {get_file_size(args.file)} KB")

if __name__ == '__main__':
    main()

# python3 Q5.py -f ../Q5/Q5.py
# python3 Q5 -d ../Q1
