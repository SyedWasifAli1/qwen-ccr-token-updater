import json
from pathlib import Path

# Paths
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
