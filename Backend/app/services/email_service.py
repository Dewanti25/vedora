import os

OUT_DIR = 'emails'
os.makedirs(OUT_DIR, exist_ok=True)

async def send_email(to_email: str, subject: str, body: str):
    # very small local placeholder that writes to a file for the MVP
    filename = f"{OUT_DIR}/{to_email.replace('@', '_at_')}_{int(__import__('time').time())}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"To: {to_email}\nSubject: {subject}\n\n{body}")
    return True
