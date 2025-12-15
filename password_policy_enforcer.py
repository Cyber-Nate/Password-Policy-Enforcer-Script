import re

def check_password_strength(password):
    rules = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    print("\nPassword Strength Check:")
    for rule, passed in rules.items():
        status = "✔ PASSED" if passed else "✘ FAILED"
        print(f"- {rule}: {status}")
        
    if all(rules.values()):
        print("\n✅ Password is STRONG")
    else:
        print("\n⚠ Password is WEAK — Improve the failed checks.")

password = input("Enter a password to test: ")
check_password_strength(password)
