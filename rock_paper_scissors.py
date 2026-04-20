"""
Create a Rock Paper Scissors game with a simple Tkinter GUI.
The player clicks a button for rock, paper, or scissors.
The game shows the computer choice, the winner, and live score.
"""
import random
import tkinter as tk


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def load_high_score():
    try:
        with open('high_score.txt', 'r', encoding='utf-8') as file:
            return max(0, int(file.read().strip() or 0))
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    with open('high_score.txt', 'w', encoding='utf-8') as file:
        file.write(str(score))


class Game:
    def __init__(self, result_label, score_label, high_score_label):
        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.high_score = load_high_score()
        self.result_label = result_label
        self.score_label = score_label
        self.high_score_label = high_score_label

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        else:
            self.tie_count += 1

        if self.player_score > self.high_score:
            self.high_score = self.player_score
            save_high_score(self.high_score)

        self.result_label.config(
            text=f"You chose {player_choice}. Computer chose {computer_choice}. {result}"
        )
        self.score_label.config(
            text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.tie_count}"
        )
        self.high_score_label.config(text=f"High Score: {self.high_score}")


def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.resizable(False, False)
    root.geometry("360x260")

    title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
    title_label.pack(pady=(12, 8))

    result_label = tk.Label(root, text="Choose rock, paper, or scissors.", font=("Arial", 11), wraplength=320)
    result_label.pack(pady=(0, 8))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=(0, 10))

    score_label = tk.Label(root, text=f"Score - You: 0, Computer: 0, Ties: 0", font=("Arial", 11))
    score_label.pack(pady=(0, 6))

    high_score_label = tk.Label(root, text=f"High Score: {load_high_score()}", font=("Arial", 11, "italic"))
    high_score_label.pack(pady=(0, 10))

    game = Game(result_label, score_label, high_score_label)

    rock_button = tk.Button(button_frame, text="Rock", width=10,
                             command=lambda: game.play('rock'))
    paper_button = tk.Button(button_frame, text="Paper", width=10,
                              command=lambda: game.play('paper'))
    scissors_button = tk.Button(button_frame, text="Scissors", width=10,
                                 command=lambda: game.play('scissors'))

    rock_button.grid(row=0, column=0, padx=6)
    paper_button.grid(row=0, column=1, padx=6)
    scissors_button.grid(row=0, column=2, padx=6)

    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=(0, 8))

    root.mainloop()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

