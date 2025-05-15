import subprocess

folders = [
    "C:\\Windows\\Temp",
    "C:\\Users\\larti\\AppData\\Local\\Temp",
    "C:\\Windows\\Prefetch"
]

print("Deleting folders (if they exist):\n")

for folder in folders:
    result = subprocess.run(f'rmdir /s /q "{folder}"',
                            capture_output=True,
                            text=True,
                            shell=True)
    
    print(f"Folder: {folder}")
    print("STDOUT:", result.stdout if result.stdout else "(no output)")
    print("STDERR:", result.stderr if result.stderr else "(no errors)")
    print("-" * 40)

# Run system file checker
print("\nRunning System File Checker (sfc /scannow)...\n")

scan = subprocess.run("sfc /scannow",
                      capture_output=True,
                      text=True,
                      shell=True)

print("Scan completed:\n")
print(scan.stdout)

if scan.stderr:
    print("Errors during scan:\n")
    print(scan.stderr)
