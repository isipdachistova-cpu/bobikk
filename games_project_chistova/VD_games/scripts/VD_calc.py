from games_project_chistova.VD_games.games.brain_calc import (
    get_question_and_answer,
    get_game_rules
)
from games_project_chistova.VD_games.scripts.VD_games import play_game


def main():
    play_game(get_game_rules, get_question_and_answer)


if __name__ == "__main__":
    main()
