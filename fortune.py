# fortune.py - Version v1.0

def main():
    print("🔮 Welcome to Harshit Chauhan's Fortune Teller (21JE0388) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Harshit! Keep smiling. ✨")
    elif mood == "sad":
        print("💫 Your fortune: Tough times don't last, but tough people do. Hang in there! 💫")
    elif mood == "neutral":
        print("🌟 Your fortune: Today is a blank canvas—make it a masterpiece. 🌟")
    else:
        print("🤔 Hmm, I don't recognize that mood. Try happy, sad, or neutral.")

if __name__ == "__main__":
    main()
