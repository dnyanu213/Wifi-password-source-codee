import subprocess

try:
    profiles = [i.split(":")[1][1:-1] for i in subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n') if "All User Profile" in i]
    
    for i in profiles:
        try:
            results = [b.split(":")[1][1:-1] for b in subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') if "Key Content" in b]
            print(f"{i:<30}|  {results[0] if results else ''}")
        except subprocess.CalledProcessError:
            print(f"{i:<30}|  ENCODING ERROR")
except subprocess.CalledProcessError:
    print("Error retrieving profiles.")

input("")
