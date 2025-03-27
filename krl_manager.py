revoked_keys = []

def revoke_key(key_name):
    if key_name not in revoked_keys:
        revoked_keys.append(key_name)
        print(f"⚠️ Key '{key_name}' Revoked!")
    else:
        print(f"⚠️ Key '{key_name}' Already Revoked!")

def check_key_status(key_name):
    return key_name in revoked_keys

def remove_key_revocation(key_name):
    if key_name in revoked_keys:
        revoked_keys.remove(key_name)
        print(f"✅ Key '{key_name}' Un-revoked!")
    else:
        print(f"❌ Key '{key_name}' Not Found in Revoked List!")