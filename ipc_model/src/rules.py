def apply_rules(text: str, ml_prediction: str) -> str:
    text = text.lower()

    # 1. Poisoning
    if any(word in text for word in ["poison", "toxic", "chemical"]):
        return "IPC 328"

    # 2. Obscene acts
    if any(word in text for word in ["obscene", "vulgar"]):
        return "IPC 294"

    # 3. Murder
    if any(word in text for word in ["killed", "death", "died"]) and any(word in text for word in ["knife", "stab", "shot", "murder", "attack"]):
        return "IPC 302"

    # 4. Attempt murder
    if "attack" in text and any(word in text for word in ["survived", "saved", "hospital", "did not die"]):
        return "IPC 307"

    # 5. Sexual assault
    if any(word in text for word in ["rape", "raped", "sexual", "forcibly", "molest", "assaulted her"]):
        return "IPC 376"

    # 6. Kidnapping
    if any(word in text for word in ["kidnap", "abduct"]):
        return "IPC 363"

    # 7. Extortion
    if "threat" in text and any(word in text for word in ["money", "pay", "amount", "ransom"]):
        return "IPC 385"

    # 8. Criminal intimidation
    if "threat" in text:
        return "IPC 506"

    # 9. Cheating
    if any(word in text for word in ["promised", "promise"]) and any(word in text for word in ["money", "amount", "paid"]) and any(word in text for word in ["never", "failed", "disappeared"]):
        return "IPC 420"

    # 10. Forgery
    if any(word in text for word in ["forged", "fake document", "signature", "stamp"]):
        return "IPC 468"

    # 11. House breaking
    if any(word in text for word in ["broke into", "entered", "house", "night"]) and any(word in text for word in ["stole", "theft", "cash", "jewellery"]):
        return "IPC 457"

    # 12. Robbery
    if any(word in text for word in ["snatch", "rob", "wallet", "mobile"]) and "force" in text:
        return "IPC 392"

    # 13. Wrongful restraint
    if any(word in text for word in ["blocked", "prevented", "restrained", "stopped"]):
        return "IPC 341"

    # 14. Dacoity with murder
    if any(word in text for word in ["gang", "armed"]) and any(word in text for word in ["rob", "loot"]) and any(word in text for word in ["killed", "death"]):
        return "IPC 396"

    return ml_prediction


