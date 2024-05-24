def bold(text):
    return f"\033[1m{text}\033[0m"


def introduction():
    print(f"""
Welcome to {bold('IntelliPass')}: Your ML-Powered Password Guardian
          
In a world where digital threats lurk around every corner, one tool stands as the ultimate guardian of your secrets: IntelliPass. Equipped with the latest advancements in artificial intelligence, IntelliPass not only stores your passwords securely but also learns and adapts to ensure your digital fortresses remain impenetrable.
""")
    

def command_help():
    print(f"""
Getting Started with SentinelAI
Command: sentinelai init

Description: Initialize SentinelAI and create your master key.
Narrative: The first step in summoning your Sentinel. Speak your master key—your voice, your command, the ultimate bond between you and your guardian.
Command: sentinelai add

Description: Add a new password entry.
Narrative: A new secret to guard? SentinelAI stands ready. Provide the details, and let your sentinel lock it away in an unbreakable vault.
Command: sentinelai retrieve

Description: Retrieve a stored password.
Narrative: Whisper the name of the secret you seek, and your sentinel will fetch it from the depths of its encrypted vault, presenting it only to you.
Command: sentinelai update

Description: Update an existing password entry.
Narrative: Even the strongest fortresses need reinforcement. Command SentinelAI to update an entry, and watch as it fortifies your defenses.
Command: sentinelai delete

Description: Delete a password entry.
Narrative: No longer need a secret? SentinelAI will ensure it is obliterated, leaving no trace behind.
Command: sentinelai audit

Description: Perform a security audit of your passwords.
Narrative: Allow SentinelAI to scan your fortresses, identifying any weak points and suggesting reinforcements to keep your defenses impenetrable.
""")
