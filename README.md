# Qwen → CCR Auto-Token-Updater-Tool

This tool reads the **Qwen OAuth access_token** from `.qwen/oauth_creds.json` and updates it automatically inside **Claude Code Router (CCR)** `config.json` under the `qwen` provider.

It works on **Windows** and **Linux**.

---

## 📁 Required Folder Location

This script must be run on a system where **both folders already exist**:

```
.qwen/
.claude-code-router/
```

These folders are usually created automatically when:

* You login using Qwen CLI
* You install and configure Claude Code Router (CCR)

---




## 🚀 Step-by-Step Setup

### ✅ Step 1: Open Command Prompt / Terminal

#### 🔹 Windows

Open **Command Prompt** or **PowerShell**:

```
Win + R → cmd → Enter
```

#### 🔹 Linux

Open **Terminal**:

```
Ctrl + Alt + T
```

---

### ✅ Step 2: Open User Home Folder (IMPORTANT)

⚠️ **Important:** `main.py` ko **project folder ke andar nahi**, balkay **direct user home directory** mai rakhna hai (jahan `.qwen` aur `.claude-code-router` already maujood hote hain).

#### 📂 Correct Location

##### 🔹 Windows

```
C:\Users\WASIF\
```

##### 🔹 Linux

```
/home/youruser/
```

Is directory ke andar hi ye folders hote hain:

```
.qwen/
.claude-code-router/
```

---

### ✅ Step 3: Open Folder in Code Editor

Ab **usi directory** ko code editor mai open karo.

Below are **3 common examples**:

#### 1️⃣ VS Code

```
code .
```

#### 2️⃣ Cursor

```
cursor .
```

#### 3️⃣ Any Editor (manual)

* Open editor
* File → Open Folder
* Select user home folder (jahan `.qwen` folder hai)

---

### ✅ Step 4: Create `main.py`

⚠️ **Important:** `main.py` **project folder ke andar nahi** balkay **direct user home directory** mai create hogi.

#### 📂 Correct Location

##### 🔹 Windows

```
C:\Users\WASIF\
└── main.py
```

##### 🔹 Linux

```
/home/youruser/
└── main.py
```





### ✅ Step 5: Copy & Paste Code into `main.py`

Paste the following code into `main.py`:

````python
import json
from pathlib import Path

# UPDATE THESE PATHS IF NEEDED
QWEN_CREDS_PATH = Path(r"C:\Users\WASIF\.qwen\oauth_creds.json")
CLAUDE_CONFIG_PATH = Path(r"C:\Users\WASIF\.claude-code-router\config.json")


def get_access_token():
    if not QWEN_CREDS_PATH.exists():
        raise FileNotFoundError("oauth_creds.json file nahi mili")

    with open(QWEN_CREDS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "access_token" not in data:
        raise KeyError("access_token key oauth_creds.json mai nahi hai")

    return data["access_token"]


def update_api_key(new_api_key):
    if not CLAUDE_CONFIG_PATH.exists():
        raise FileNotFoundError("config.json file nahi mili")

    with open(CLAUDE_CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    providers = config.get("Providers", [])

    for provider in providers:
        if provider.get("name") == "qwen":
            old_key = provider.get("api_key", "N/A")

            print("""
╔══════════════════════════════════╗
║   Developed by Syed Wasif Ali    ║
║   AI • Full-Stack • Cloud        ║
╚══════════════════════════════════╝
""")

            print("\n🔑 OLD API KEY:")
            print(old_key)

            print("\n🔑 NEW API KEY (from access_token):")
            print(new_api_key)

            provider["api_key"] = new_api_key
            break
    else:
        raise ValueError("qwen provider config.json mai nahi mila")

    with open(CLAUDE_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print("\n✅ api_key successfully update ho gaya\n")


def main():
    try:
        access_token = get_access_token()
        update_api_key(access_token)
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
````

---

### ✅ Step 6: Update Paths (IMPORTANT)

Update these two lines according to **your system user directory**:

#### 🔹 Windows Example

```
QWEN_CREDS_PATH = Path(r"C:\Users\YOUR_NAME\.qwen\oauth_creds.json")
CLAUDE_CONFIG_PATH = Path(r"C:\Users\YOUR_NAME\.claude-code-router\config.json")
```

#### 🔹 Linux Example

```
QWEN_CREDS_PATH = Path("/home/youruser/.qwen/oauth_creds.json")
CLAUDE_CONFIG_PATH = Path("/home/youruser/.claude-code-router/config.json")
```

👉 **Rule:**
Paths should point to the directory where `.qwen` and `.claude-code-router` folders exist.

---

### ✅ Step 7: Run the Script

```
python main.py
```

---

## 🎯 Expected Output

```
🔑 OLD API KEY:
xxxxxxxxxx

🔑 NEW API KEY (from access_token):
eyJhbGciOi...

✅ api_key successfully update ho gaya
```

---

## 🧠 What This Tool Does (Simple)

```
.qwen/oauth_creds.json
        ↓
reads access_token
        ↓
.claude-code-router/config.json
        ↓
Providers → qwen → api_key updated
```

---

## ✅ Use Case

* Qwen OAuth token auto-sync
* CCR Qwen provider always up-to-date
* No manual copy-paste of API keys

---

## 🔁 Token Refresh Flow (IMPORTANT)

### 🆕 First Time Setup

* Ye setup **sirf pehli baar** required hota hai
* Jab `main.py` create ho jaye aur paths set ho jayein, us ke baad structure ready hota hai

---

### 🔄 Jab Bhi Token Update Karna Ho

Har baar Qwen ka token refresh karne ke liye **ye exact flow follow karo**:

1️⃣ **Qwen start karo**

```
qwen
```

2️⃣ Qwen start hote hi token generate ho jata hai

3️⃣ Ab Qwen ko **stop karo**:

```
Ctrl + C
```

ya

```
/quit
```

4️⃣ Ab token `.qwen/oauth_creds.json` mai update ho chuka hota hai

5️⃣ Ab Python script run karo:

```
python main.py
```

👉 Is se naya Qwen `access_token` automatically **CCR ke config.json** mai update ho jaye ga

---

## 🛑 Notes

* Make sure Qwen installed & logged in ho
* CCR pehle se installed hona chahiye
* Qwen ko start kiye baghair token update nahi hota
* Script ko har token expiry ke baad dobara run kar sakte ho

---

Happy Coding 🚀
