class TicTacToe:
    def __init__(self):
        self.player_options = ("x", "o")
        self.turn_counter = 0
        self.current_player = "x"
        self.valid_plays = list(range(9))
        self.is_winner = False
        self.winner = None
        self.play_history = {'x': [], 'o': []}
        self.board = self.create_board()

        while self.is_winner == False:
            self.next_move()
            self.turn_counter += 1
            self.is_winner = self.check_for_winner()
            self.winner = self.current_player
            self.current_player = self.player_options[self.turn_counter % 2]

        print(f"Congrats player {self.winner}, you've won!")


    def create_board(self):
        """creates a 3x3 board size with nested lists"""
        return [['_'] * 3 for ii in range(3)]

    def display_current_board(self):
        board_txt = ""
        for ii, row in enumerate(range(len(self.board))):
            board_txt += f"{self.board[row][0]}|{self.board[row][1]}|{self.board[row][2]}\n"
        print(board_txt)

    def confirm_valid_move(self, play_num):
        valid_move = play_num in self.valid_plays
        return valid_move


    def next_move(self):
        self.display_current_board()
        input_txt = f"Player {self.current_player}, pick where to play next then press ENTER."
        play_here = int(input(input_txt))

        # Confirm can move in correct location
        valid_play = self.confirm_valid_move(play_here)
        while not valid_play:
            input_txt = f"Player {self.current_player}, please select a valid play location."\
                        f"\n{self.valid_plays}"
            play_here = int(input(input_txt))
            valid_play = self.confirm_valid_move(play_here)

        self.update_board(input_space=play_here)

    def update_board(self, input_space):
        def convert_input_space_to_board_idx(input_space):
            return (input_space//3, input_space%3)
        board_idx = convert_input_space_to_board_idx(input_space)
        self.board[board_idx[0]][board_idx[1]] = self.current_player
        
        # update play status for each round
        self.play_history[self.current_player].append(input_space)
        self.valid_plays = sorted(list(set(self.valid_plays) - set([input_space])))

    def check_for_winner(self):
        curr_player_play_history = self.play_history[self.current_player]
        ways_to_win = [[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8],
                       [0, 3, 6],
                       [1, 4, 7],
                       [2, 5, 8],
                       [0, 4, 8],
                       [2, 4, 6]]
        winner = False
        for win_combo in ways_to_win:
            if set(win_combo).issubset(set(curr_player_play_history)):
                winner=True
                break
        return winner

if __name__ == "__main__":
    game = TicTacToe()

