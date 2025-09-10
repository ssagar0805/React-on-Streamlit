import os

# List of folders or files to ignore
IGNORE_FOLDERS = {'.git', '__pycache__'}
IGNORE_EXTENSIONS = {'.pyc', '.log', '.tmp'}

def print_clean_file_tree(start_path, indent=''):
    for item in os.listdir(start_path):
        path = os.path.join(start_path, item)
        # Skip ignored folders
        if os.path.isdir(path):
            if item not in IGNORE_FOLDERS:
                print(f"{indent}📁 {item}/")
                print_clean_file_tree(path, indent + '    ')
        else:
            # Skip ignored file extensions
            if not any(item.endswith(ext) for ext in IGNORE_EXTENSIONS):
                print(f"{indent}📄 {item}")

# Replace with your project path
root_path = r"D:\Technocrats 2.0\MAIN Streamlitlib Project\MAIN-Streamlitlib-Working-"
print(f"Clean File Tree for: {os.path.abspath(root_path)}\n")
print_clean_file_tree(root_path)
