import random
import time

def clear_screen():
    print("\n" * 50)

def start_game():
    print("=== WELCOME TO THE IMPOSTER GAME! ===")
    print("Rules: Each round, two players get the same word, and one player (the Imposter) gets a different but similar word.")
    print("Everyone will give a clue without saying their exact word.")
    print("If the innocents find the imposter, they get 500 points. If not, the imposter gets 500 points!\n")

    players = []
    for i in range(1, 4):
        name = input(f"Enter name for Player {i}: ")
        players.append(name)

    scores = {player: 0 for player in players}

    rounds = [
        {"category": "Animals", "words": ("Dog", "Cat")},
        {"category": "Foods", "words": ("Pizza", "Burger")},
        {"category": "Mythical Creatures", "words": ("Dragon", "Dinosaur")}
    ]

    for round_num, round_data in enumerate(rounds, 1):
        print(f"\n--- ROUND {round_num}: {round_data['category'].upper()} ---")
        time.sleep(1)
        
        main_word, imposter_word = round_data["words"]
 
        imposter = random.choice(players)
    
        for player in players:
            input(f"\nIt's {player}'s turn. Others look away! (Press Enter to view)")
            if player == imposter:
                print(f"Your word is: {imposter_word}")
            else:
                print(f"Your word is: {main_word}")
            
            input("Press Enter to hide your word...")
            clear_screen()
            
        print("\nTime for clues!")
        print("Everyone, take turns giving a subtle clue about your word.")
        
        for player in players:
            clue = input(f"{player}, type your clue: ")
            print(f"> {player} says: '{clue}'")
            
        print("\nVoting Time!")
        print("Who do you think is the imposter?")

        votes = {player: 0 for player in players}
        for player in players:
            vote = input(f"{player}, who is the imposter? (Type name): ")
            if vote in votes:
                votes[vote] += 1
                
        most_voted = max(votes, key=votes.get)
        
        print("\nRevealing results...")
        time.sleep(2)
        print(f"The real Imposter was: {imposter}!")

        if most_voted == imposter:
            print("Congratulations! You found the imposter. Innocents win 500 points each!")
            for player in players:
                if player != imposter:
                    scores[player] += 500
        else:
            print("Unfortunately, you failed! The imposter fooled you and wins 500 points!")
            scores[imposter] += 500

        print("\n--- CURRENT SCORES ---")
        for player, score in scores.items():
            print(f"{player}: {score} Points")
        print("-" * 25)
        time.sleep(2)

    print("\n" + "=" * 30)
    print("GAME OVER!")
    print("TOTAL SCOREBOARD:")
    for player, score in scores.items():
        print(f"{player}: {score} Points")
        
    winner = max(scores, key=scores.get)
    highest_score = scores[winner]

    winners = [player for player, score in scores.items() if score == highest_score]
    
    print("\n" + "*" * 30)
    if len(winners) > 1:
        print(f"CONGRATULATIONS! IT'S A TIE! WINNERS: {', '.join(winners)} ({highest_score} Points)")
    else:
        print(f"CONGRATULATIONS {winner.upper()}! YOU ARE THE WINNER! ({highest_score} Points)")
    print("*" * 30)

if __name__ == "__main__":
    start_game()
