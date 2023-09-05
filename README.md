# Chess in Python 3.1 by Burak Kucuktopal

## Setup
### Cloning the repository
<ol>
  <li>Go to you command prompt</li>
  <li>Enter "cd.." in your prompt until you have "C:\>" </li>
  <li> Drag the folder to which you'd like to go to your folder and change the "C:" that will automatically appear at the front to "cd"</li>
  <li>Clone the repository. This means copying and pasting following line in your command prompt: </li>
  
  ```
  git clone https://github.com/BurakKTopal/Chess.git
  ```
  
  <li>After the clone happened succesfully. Open the project with an IDE, such as PyCharm, install the necessary packages(see next) and you're ready to play!</li>
</ol>

### Required libraries
To run the program properly, following packages must be installed:
<ul>
  <li>pygame, for visualisation</li>
  <li>time, for timing the amount of time needed to generate move</li>
  <li>numpy, for calculating sign of values(used for color identification)</li>
  <li>random, for the Zobrist keys generation</li>
  <li>chessboard(if this gives nothing, try chess-board), for the Zobrist keys generation</li>
  <li>display from chessboard, for the Zobrist keys generation</li>  
</ul>
<p>
  This is done via the terminal with use of <a href = https://pip.pypa.io/en/stable/installation/>pip</a>.
</p>
In case of pip, type in your terminal of the IDE:

```
pip install pygame time numpy random chess-board chessboard display
```

## The Begin of a challenge
<p>
I got interested in playing chess at my 13th and really started playing when I was 14 years old. At the age of 16 I became regional champion of my age category, and on my 17th of all age categories. But my eager to play chess has declined since then. To revive this and improve my Python class comprehension, I started making a chess program in March 2023. Two hard weeks resulted in a program in which a move be played by given in the console the move, conform to the general chess notation. There was not yet a engine, and it was certainly not optimized, nor user friendly; not everyone knows proper chess notation. I knew I had some clean up to do, as it was a complex cluster of if and for loops and not even commented. At the time though, it worked, so I was happy. I knew one day I'd need to clean it up etc. to present it properly...
</p>

<p>
August 15, I started looking back into my program. At first sight it was really a big chaos; it costed me, the maker of the program, 2 days(!) to go through it and clean it up. I wrote a program to count the number of positions available for a certain depth. At depth 4 from the begin position, it took 23 minutes to count the 197 281 positions! The number seems impressive, but the time it takes to achieve this is gigantically poor; it would mean $\approx$ 194 nodes/s. Compare this miserable number to that of the super-engine <a href = "https://chessify.me/blog/nps-what-are-the-nodes-per-second-in-chess-engine-analysis">Stockfish</a>: $5 \cdot 10^{6} - 2 \cdot 10^{7}$ nodes/s. As from here, the optimization journey begins!
</p>

## Optimization of internal processes

### Proper Python class use
<p>
When I started looking back at the code in August, the first thing I notices was the very improper use of Python classes. Each time I needed a function that was created in the board class, I'd would make a new instance of the class and call the function. This is equal to creating mutliple boards instead of working with one! 
</p>

### Saving king positions
<p>
Once I understood that I can give characteristics to the board, I started saving the positions of the king. This comes handy when you consider looking for checks: instead of each time searching through all 64 squares for the king of the corresponding color, I can just fetch it from the board-object.
</p>

### Breaking loop if condition already satisfied
<p>
One of the ways to look if a move by a piece is legal, is to check if there are any pieces between the begin and endpoint. If there is, then the move could not be played; as pieces, excluding the knight, cannot jump over other pieces. I previously continued the loop, even if a piece was already found on the path, but I finally realized that it could be stopped if at least one was found.
</p>

### Saving the non-empty cells
<p>
Inspired by the <a href ="https://www.youtube.com/watch?v=U4ogK0MIzqk"> video </a> of <a href = "https://github.com/SebLague/Chess-Coding-Adventure"> Sebastian League</a>, I started saving the non-empty cells on the board. This strongly improves the time to generate the possible moves, since there will be at least 32 squares not checked anymore.
</p>

### Line of sight
To come up with this one, it took me quite some time. The function 'if_in_check()' looks if the king is in check and 'looking_if_check()' plays a move and looks if it results in seting his own king in check, if so, then the move is not legal. 'looking_if_check()' was first called every time a move is validated, but this is only needed for the pieces which are in the line of sight of the king! This means that a friendly piece that is NOT diagonally, horizontally or vertically connected to the king, cannot put his own king in check. This reduced the number of calls to the 'if_in_check()' function, and thus reduced the time.

### Performance <-> time
After these modifications, the number of nodes/s achieved drastically increased. As stated in the begin, my program counted 197 281 positions in 23 minutes at depth 4. Now it counted 197 702 positions in 129 seconds, giving $\approx$ 1532 nodes/s! But comparing this number to that of <a href = "https://en.wikipedia.org/wiki/Shannon_number"> Shannon's number</a>, we see an offset of 421. This is 0.002 of the counted positions. You'd think that this won't give a problem in the future, but that is a faulty thought! The begin positions doesn't contain that much complex moves, and thus even the smallest offset could cause big problems once going live. But I had honestly a bit enough of debugging and wanted to work on the user-interface: making an interactive chess board instead of giving in cryptic chess notations in the console.

## User-interface
The UI is achieved by making use of pygame. By entering a menu, the person can choose which format he'd like to play:
<ul>
  <li>Multiplayer: playing on one screen against another person</li>
</ul>
 Against the engine:  
  <ul>
        <li>Person plays white</li>
        <li>Person plays black</li>
  </ul>

<p>
  Now it is time to introduce the algorithm to play against the human!
</p>

## Engine incorporation
Originally when I started with this project, I had deep AI in mind. But for the time being, I avoided this and looked at other techniques to make an engine. For a two-player game the first choice falls for the minimax algorithm. Before diving into this, there is need to talk about the evaluation in chess games.

### Evaluating a chess position
<p>
There are different way to analyze a chess position. To start evaluating, there is first need to give values to the pieces, for white this is:
</p>
<ul>
  <li>Pawn: 1</li>
  <li>Knight: 3</li>
  <li>Bishop: 3</li>
  <li>Rook: 5</li>
  <li>Queen: 9</li>
  <li>King: 100</li>
  <li>For black it's the same value, only with a reversed sign</li>
</ul>
<p>
With these points in mind, a naive approach is by adding all the pieces' points on the board and look if it is positive or negative to see which side is better and by how much. This is a good estimator when
  you'd like to have a <a href = "https://chessify.me/blog/chess-engine-evaluation">global assessment</a> of the position by looking at this number. But this won't give any hint to the engine how to play the opening; the fundament of the game. To account for this, I've made use of square-piece tables. I first started using these tables for the whole game, but I quickly understood that the engine couldn't play the endgame properly. To account for this, I've made use of the <a href="https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function"> PeSTO's evaluation tables</a>, modified it a bit, for the endgame and used the tables I'd already had as a guide for the engine during the middlegame.
</p>
<p>
  Further improvements regarding the evaluation could be:
  <ul>
    <li>Adding 'activity function' that serves as to give more points to pieces that are more active; meaning there have control over more square.</li>
    <li>Adding an opening book to ensure the opening goes as smooth as possible</li>
    <li>Adding AI functionality which adds/decreases notches of pionts based on earlier seen positions.</li>
  </ul>
</p>

### Algoritmhs
<p>
  There has to be a plan that the engine needs to follow to determine the best move. This can be done by several ways(AI, minimax, negamax, ...). In my program
  I have made use of minimax and some modifications on it.
</p>

#### Minimax without pruning
<p>
Minimax relies on the principle of a maximizing(white) and minimizing(black) the evaluation of the position. This algorithm goes through all possible positions for a given depth and determines, based on the given evaluation function, which positions is the most favourable for the engine.
</p>

####  Minimax with pruning
<p>
In a game of chess, going through all different positions is very time-expensive when we're going to higher depths. To counter this, we can 'prune' the game tree. A game tree represents per level the possible chess positions that can be achieved. The pruning happens by working with additional $\alpha$ and $\beta$ parameters. With these parameters we could stop searching further into a branch of the tree if we're pretty sure that it won't give any better move. We thus 'prune' the branch. Sebastian League again made a fantastic <a href="https://www.youtube.com/watch?v=l-hh51ncgDI&t">video</a> about this topic. 
</p>

#### Minimax with pruning and Zobrist Hashing
<p>
With the pruning, we can already achieve a decent chess engine, but I wanted to do something extra to make it a notch faster. This can be achieved by the concept of 'Hashing'. Hashing in this case means that you map a chess position to a unique number and save this as a key in a dictionary with its value information about the position; $\alpha$, $\beta$, best move and evaluation. This comes very handy in chess because of the phenomena called 'transpositions'. For example for a depth of 4: we can have the game 1.e4 2.e5 3.Nc3 and 1.Nc3 2.e5 3.e4 If you'd play this out, you'll see that we have the exact same position. In this case, by rememebering that the engine already encountered this position in previous calculations, it can gather the information of the position out of the dictionary.
</p>

##### Zobrist Hashing
<p>
Zobrist hashing is pretty straightforward. You generate a random number, for enough arbitrariness I've chosen integers between 0 and 10E10, for each piece on each square of the chess board. Thus you have a list containing 64 dictionaries and each dictionary having 12 keys. Besides, you also generate 8 random numbers for each column for en passant as you can have visually the same chess position, but differing because in one you can play en passant, and the other not. Finally you generate 4 random numbers for the castling(long and short for white, and long and short for black). Once you've generated the 'Zobrist Keys', you can apply this on a given chess position. By going through all the <strong>non-empty squares</strong>, you look which piece is on it, take the random number corresponding to that piece on that square and then you XOR all the number with eachother. At the end, you'll get a number, which is the Zobrist Key of that position.
</p>
<p>
  Note that the generation of the random numbers is a one time action and can then be used as seed for further Zobrist Key generation.
</p>

## Choosing the difficulty and type of algorithm when playing
<p>
  You can also choose the difficulty of the engine and on which algorithm it runs. You can choose out of the three algorithms:
  <ul>
              <li>minimax_with_zobrist_hashing_no_pruning(chessboard, depth, maximizingPlayer): this is minimax, with NO
                    PRUNING, but WITH zobrist hashing</li>
    
              <li> minimax_with_pruning(chessboard, depth, -float('inf'), float('inf'), maximizingPlayer):
                    This is the famous alpha-beta-pruning, but WITHOUT the zobrist hashing </li>
                    
              <li> minimax_with_zobrist_hashing_and_pruning(chessboard, depth, -float('inf'), float('inf'), maximizingPlayer):
                    this is minimax, PRUNED and WITH the zobrist hashing</li>
  </ul>
</p>





