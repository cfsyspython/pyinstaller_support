import os

def find_all_py_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        if ".git" in root or ".idea" in root or "temp" in root or ".venv" in root:
            continue
        for file in files:
            if file=="List_of_py&nonpy_files.py":
                continue
            if file.endswith('.py'):
                # Remove the base directory path from the file path
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                # Normalize the path
                a = relative_path.split("\\")
                new = ""
                for i, j in enumerate(a):
                    if i > 0:
                        new += "/" + j
                    else:
                        new += j

                py_files.append(new)
    return py_files

def find_all_non_py_files(directory):
    non_py_files = []
    for root, _, files in os.walk(directory):
        if ".git" in root or ".idea" in root or "temp" in root or  ".venv" in root or  "build" in root or "dist" in root:
            continue
        for file in files:
            if file=="main.spec" or file=="piSetting.txt" or file=="requirements.txt" or file=="test.txt" or file==".gitignore":
                continue
            if not file.endswith('.py'):
                # Remove the base directory path from the file path
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                # Normalize the path
                print(root,"\n",_,"\n",file,"\n\n")
                a = root.split("\\")
                new = ""
                for i, j in enumerate(a):
                    if i > 0:
                        new += "/" + j
                    else:
                        new += j
                dire=""
                folder=root.split("py_treding")[1].split("\\")
                print(folder)
                for i, j in enumerate(folder):

                    if i > 0:
                        dire += "/" + j
                    else:
                        dire += j
                non_py_files.append(eval(f'''("{new}/{file}","{dire}")'''))
    return non_py_files

# Specify the directory to search
directory_to_search = os.getcwd().split('temp')[0]

# Find all Python files
python_files = find_all_py_files(directory_to_search)
print("py: ",python_files)

# Find all non-Python files
non_py_files = find_all_non_py_files(directory_to_search)
print("nonpy: ",non_py_files)
