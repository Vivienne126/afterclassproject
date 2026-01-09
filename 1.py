import random
from collections import defaultdict

moves = ["rock", "paper", "scissors"]

# What beats what
beats = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

# Store history
player_history = []
transition_table = defaultdict(lambda: defaultdict(int))

player_score = 0
ai_score = 0

def predict_player_move():
    # If not enough data, guess randomly
    if len(player_history) < 2:
        return random.choice(moves)

    last_move = player_history[-1]

    # Use transition table (Markov logic)
    if transition_table[last_move]:
        predicted = max(
            transition_table[last_move],
            key=transition_table[last_move].get
        )
        return predicted

    # Fallback: most frequent move
    return max(set(player_history), key=player_history.count)

def ai_move():
    predicted_player = predict_player_move()
    return beats[predicted_player]

def decide_winner(player, ai):
    if player == ai:
        return "draw"
    elif beats[player] == ai:
        return "ai"
    else:
        return "player"

print("🤖 Advanced Rock Paper Scissors AI 🤖")
print("Type rock, paper, scissors or quit\n")

while True:
    player = input("Your move: ").lower()

    if player == "quit":
        break

    if player not in moves:
        print("❌ Invalid move")
        continue

    if player_history:
        transition_table[player_history[-1]][player] += 1

    player_history.append(player)

    ai = ai_move()
    print(f"AI chose: {ai}")

    winner = decide_winner(player, ai)

    if winner == "player":
        player_score += 1
        print("✅ You win!")
    elif winner == "ai":
        ai_score += 1
        print("🤖 AI wins!")
    else:
        print("⚖️ It's a draw!")

    print(f"Score → You: {player_score} | AI: {ai_score}")
    print("-" * 30)

print("\nGame Over")
print(f"Final Score → You: {player_score} | AI: {ai_score}")
