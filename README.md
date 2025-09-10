# 🗑️ secure-delete-cli

A simple Python CLI tool to securely delete files by overwriting them with random data before removal.

## ✨ Features
- Overwrites files multiple times with random data
- Works on any file type
- Configurable number of overwrite passes
- Lightweight, no external dependencies

## 🚀 Installation
Clone the repository:

    git clone https://github.com/brandonkkip000-web/secure-delete-cli.git
    cd secure-delete-cli

No extra dependencies are needed (Python standard library only).

## 🛠️ Usage

### Securely delete a file
    python secure_delete.py secret.txt

➡️ Overwrites secret.txt with random data 3 times, then deletes it.

### Custom overwrite passes
    python secure_delete.py secret.txt --passes 5

➡️ Overwrites the file 5 times before deletion.

## ⚠️ Notes
- This tool reduces the chances of recovery but does not guarantee protection against advanced forensic tools.
- For sensitive data, use full-disk encryption in addition to secure deletion.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author
**Brandon**  
[GitHub Profile](https://github.com/brandonkkip000-web)
