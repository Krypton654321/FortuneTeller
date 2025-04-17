# fortune.py - Version v1.1

import random

def main():
    print("🔮 Welcome to Harshit Chauhan's Fortune Teller (21JE0388) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "Great things await you, Harshit! Keep smiling.",
            "Your joy is contagious—spread it around!"
        ],
        "sad": [
            "Every storm runs out of rain. Better days are coming.",
            "You are stronger than you think."
        ],
        "neutral": [
            "Sometimes peace is its own reward.",
            "Today might surprise you—stay open to it."
        ],
        "stressed": [
            "Take a deep breath. You've got this.",
            "Harshit, even the busiest bees take a break!"
        ]
    }

    if mood in fortunes:
        print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
    else:
        print("🤔 Hmm, I don't recognize that mood. Try happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    main()
