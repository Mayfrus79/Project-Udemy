import os
import shutil
import subprocess

folders = [
    r"C:\\Windows\\Temp",
    os.path.expandvars(r"%LOCALAPPDATA%\\Temp"),
    r"C:\\Windows\\Prefetch",
]

for folder in folders:
    if not os.path.exists(folder):
        print(f"{folder} does not exist.")
        continue

    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        try:
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                os.remove(path)
        except Exception as e:
            print(f"Failed to delete {path}: {e}")

# Run System File Checker
try:
    result = subprocess.run(["sfc /scannow"], capture_output=True, text=True, shell=False)
    print(result.stdout)
except Exception as e:
    print(f"Error running sfc: {e}")
