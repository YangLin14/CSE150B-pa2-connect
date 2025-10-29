def minmax(game, depth, use_alpha_beta, evaluator, alpha, beta):
    if game.is_terminal():
        winner = game.winner()
        if winner == 'R':
            return float('inf'), None
        elif winner == 'Y':
            return float('-inf'), None
        else:
            return evaluator(game), None
    
    if depth == 0:
        return evaluator(game) if evaluator is not None else 0, None
    
    is_maximizing = (game.player == 'R')

    if is_maximizing:
        best_score = float('-inf')
        best_move = None

        for action in game.legal_actions():
            new_game = game.clone()
            new_game.play(action)
            score, _ = minmax(new_game, depth - 1, use_alpha_beta, evaluator, alpha, beta)

            if score > best_score:
                best_score = score
                best_move = action

            if use_alpha_beta:
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None

        for action in game.legal_actions():
            new_game = game.clone()
            new_game.play(action)
            score, _ = minmax(new_game, depth - 1, use_alpha_beta, evaluator, alpha, beta)

            if score < best_score:
                best_score = score
                best_move = action

            if use_alpha_beta:
                beta = min(beta, best_score)
                if beta <= alpha:
                    break

        return best_score, best_move

def best_move(game, depth=3, use_alpha_beta=True, evaluator=None):
    alpha = float('-inf')
    beta = float('inf')

    score, action = minmax(game, depth, use_alpha_beta, evaluator, alpha, beta)

    if action is None and not game.is_terminal():
        return game.legal_actions()[0]

    return action


"""
I asked Gemini:
I got this error what does this mean?
Exception in Tkinter callback
Traceback (most recent call last):
  File "/opt/anaconda3/envs/cse150b/lib/python3.11/tkinter/__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/envs/cse150b/lib/python3.11/tkinter/__init__.py", line 861, in callit
    func(*args)
  File "/Users/yanglin/Documents/UCSD/Fall 2025/CSE150B/CSE150B-pa2-connect/connectx/app.py", line 36, in ai_turn
    g.play(mv); draw()
    ^^^^^^^^^^
  File "/Users/yanglin/Documents/UCSD/Fall 2025/CSE150B/CSE150B-pa2-connect/connectx/game.py", line 12, in play
    if self.board[r][col] is None:
       ~~~~~~~~~~~~~^^^^^
TypeError: list indices must be integers or slices, not NoneType

Gemini's response:
This is a classic and subtle bug! Here's what's happening.

What the Error Means
The error TypeError: list indices must be integers or slices, not NoneType means that 
your code tried to access an item in a list using None as the index, like my_list[None]. 
Python lists only accept integers (like my_list[0]) or slices (like my_list[1:3]) as indices.

How to fix it:
Add the following to your best_move function

if action is None and not game.is_terminal():
        return game.legal_actions()[0]
"""