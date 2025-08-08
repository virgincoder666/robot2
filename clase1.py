# italian_brainrot.py
import random, time, sys, shutil, os

EMOJIS = ["🇮🇹", "🍝", "🫴", "🍕", "🛵", "💥", "🧄", "🧀", "🍷"]
INTERJECCIONS = [
    "Mamma mia", "Ma che cosa", "Ayooo", "Capisce", "Porca miseria",
    "Andiamo", "Bellissimo", "Amore mio", "Gabagool moment", "Spaghettification"
]
PASTAS = ["spaghetti", "rigatoni", "penne", "farfalle", "fettuccine", "orecchiette", "gnocchi", "ravioli", "tortellini"]
SUFFIXES = ["-ini", "-etto", "-uccio", "-issimo", "-one", "-etta"]

# --- ANSI colors ---
RESET = "\033[0m"
COLORS = ["\033[92m", "\033[91m", "\033[93m", "\033[95m", "\033[96m", "\033[94m"]

def colorize(s: str) -> str:
    return random.choice(COLORS) + s + RESET

def double_vowels(word: str) -> str:
    out = []
    for ch in word:
        if ch.lower() in "aeiou":
            out.append(ch * random.choice([2,2,3]))  # sesgo a duplicar
        else:
            out.append(ch)
    return "".join(out)

def italianize(text: str) -> str:
    words = text.split()
    spiced = []
    for w in words:
        base = double_vowels(w)
        if random.random() < 0.6:
            base += random.choice(SUFFIXES)
        spiced.append(base)
        if random.random() < 0.25:
            spiced.append(random.choice(EMOJIS))
    # mete interjecciones al inicio/fin
    start = random.choice(INTERJECCIONS)
    end = random.choice(["capisce?", "per favore", "grazie", "mamma mia...", "no cap— sì capisce!"])
    return f"{start}! " + " ".join(spiced) + f" — {end} " + random.choice(EMOJIS)

def brainrot_sentence() -> str:
    tpls = [
        "Io vedo {pasta} con {pasta}, {interj}! {emoji}{emoji}",
        "No thoughts, only {pasta} {emoji} {interj} 🫴",
        "{interj}! This code runs on pure {pasta} energy {emoji}",
        "If it ain't {pasta}, I don't wanna hear it {emoji}",
        "Certified {pasta}-lover moment {emoji} {interj}",
    ]
    tpl = random.choice(tpls)
    return tpl.format(
        pasta=random.choice(PASTAS),
        interj=random.choice(INTERJECCIONS),
        emoji=random.choice(EMOJIS),
    )

def stream_brainrot(duration=8):
    t_end = time.time() + duration
    print(colorize("▶ Italian Brainrot Stream (Ctrl+C para parar)\n"))
    try:
        while time.time() < t_end:
            s = brainrot_sentence()
            print(colorize(s))
            time.sleep(random.uniform(0.25, 0.7))
    except KeyboardInterrupt:
        pass
    print(RESET)

def animate_hand(cycles=2, speed=0.01):
    hand = "🫴"
    pasta = random.choice(PASTAS)
    print(colorize(f"\n{random.choice(INTERJECCIONS)}! Mira la manita diciendo '{pasta.upper()}!!'"))
    cols = shutil.get_terminal_size((80, 20)).columns
    width = max(20, cols - 2)
    try:
        for _ in range(cycles):
            for x in range(width):
                line = " " * x + hand + "  " + colorize(pasta.upper() + "!!")
                sys.stdout.write("\r" + line[:width])
                sys.stdout.flush()
                time.sleep(speed)
            for x in range(width, 0, -1):
                line = " " * x + hand + "  " + colorize(pasta.upper() + "!!")
                sys.stdout.write("\r" + line[:width])
                sys.stdout.flush()
                time.sleep(speed)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\r" + " " * width + "\r")
        print(colorize("Finito. 🍝"))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()
    print(colorize("=== ITALIAN BRAINROT 3000 🇮🇹===\n"))
    print("1) Italianizar mi texto")
    print("2) Stream de frases brainrot")
    print("3) Animación de la manita 🫴")
    print("4) Salir\n")

def main():
    while True:
        menu()
        op = input("Elige una opción (1-4): ").strip()
        if op == "1":
            txt = input("\nEscribe algo para italianizar: ")
            print("\n" + colorize(italianize(txt)) + "\n")
            input("Enter para volver al menú...")
        elif op == "2":
            dur = input("Duración en segundos (default 8): ").strip()
            dur = int(dur) if dur.isdigit() else 8
            stream_brainrot(dur)
            input("Enter para volver al menú...")
        elif op == "3":
            animate_hand()
            input("Enter para volver al menú...")
        elif op == "4":
            print(colorize("\nArrivederci! 🍷"))
            break
        else:
            print("Opción no válida."); time.sleep(1)

if __name__ == "__main__":
    main()
