BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def rps_winner(player_1: str, player_2: str) -> str:
    if player_1 == player_2:
        return "tie"
    if player_2 == BEATS[player_1]:
        return "player one"
    return "player two"


if __name__ == "__main__":
    assert rps_winner("rock", "paper") == "player two"
    assert rps_winner("rock", "scissors") == "player one"
    assert rps_winner("paper", "scissors") == "player two"
    assert rps_winner("paper", "rock") == "player one"
    assert rps_winner("scissors", "rock") == "player two"
    assert rps_winner("scissors", "paper") == "player one"
    assert rps_winner("rock", "rock") == "tie"
    assert rps_winner("paper", "paper") == "tie"
    assert rps_winner("scissors", "scissors") == "tie"
