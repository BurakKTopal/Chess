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
August 15, I started looking back into my program. At first sight it was really a big chaos; it costed me, the maker of the program, 2 days(!) to go through it and clean it up. I wrote a program to count the number of positions available for a certain depth. At depth 4 from the begin position, it took 23 minutes to count the 197 281 positions! The number seems impressive, but the time it takes to achieve this is gigantically poor; it would mean $\approx$ 194 nodes/s. Compare this miserable number to that of the super-engine <a href = https://chessify.me/blog/nps-what-are-the-nodes-per-second-in-chess-engine-analysis>Stockfish</a>: $5 \cdot 10^{6} - 2 \cdot 10^{7}$ nodes/s. As from here, the optimization journey begins!
</p>

## Optimization

### Proper Python class use
When I started looking back at the code in August, the first thing I notices was the very improper use of Python classes, as an example:




