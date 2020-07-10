# Tic-Tac-Toe

The game tic-tac-toe to play against AI created using minimax algorithm. 
Please run the main.py code to start the application.

## AI
The AI in this game uses mini-max algorithm to find the best move. Here it finds all the posibilites and chooses the right move automatically, and no proper rules are fed manually to the AI.

### Mini-Max Algorithm 

This is a decision tree based algorithm which traverses through all the combinations to reduce or increase the evaluation for each combination. The end-node evaluation metric is `eval = 10 - depth` if the result is a win for AI and `eval = -10 + depth` if the result is a lose for AI. This makes the algorithm searches for the best solution at least depth possible. The algorithm always looks for the best move, so any game with the AI will always end in a draw or lose.

Since this algorithm has to compare all the combinations to get to a decision, the time consumption is so high. To resolve this issue, **Alpha-Beta pruning** is used. 

## Reference
* [Minimax algorithm and alpha beta pruning](https://youtu.be/l-hh51ncgDI)
