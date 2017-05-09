<div class="markdown"><p>An <em>amazon</em> (also known as a <em>queen+knight compound</em>) is an imaginary chess piece that can move like a queen or a knight (or, equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon attacks from <code>e4</code> (circles represent knight-like moves while crosses correspond to queen-like moves).</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/amazonCheckmate/img/amazon.png?_tm=1490625459392" alt=""></p>
<p>Recently you've come across a diagram with only three pieces left on the board: a white <em>amazon</em>, white king and black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black's king, so it looks like you'll have to check them all.</p>
<p>Given the positions of white pieces on a standard chessboard, determine the number of possible black king's positions such that:</p>
<ul>
<li>it's checkmate (i.e. black's king is under <em>amazon's</em> attack and it cannot make a valid move);</li>
<li>it's check (i.e. black's king is under <em>amazon's</em> attack but it can reach a safe square in one move);</li>
<li>it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);</li>
<li>black's king is on a safe square and it can make a valid move.</li>
</ul>
<p>Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>king = "d3"</code> and <code>amazon = "e4"</code>, the output should be<br>
<code>amazonCheckmate(king, amazon) = [5, 21, 0, 29]</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/amazonCheckmate/img/example1.png?_tm=1490625459585" alt=""></p>
<p>Red crosses correspond to the checkmate positions, orange pluses refer to checks and green circles denote safe squares.</p>
</li>
<li>
<p>For <code>king = "a1"</code> and <code>amazon = "g5"</code>, the output should be<br>
<code>amazonCheckmate(king, amazon) = [0, 29, 1, 29]</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/amazonCheckmate/img/example2.png?_tm=1490625459719" alt=""></p>
<p>Stalemate position is marked by a blue square.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string king</strong></p>
<p>Position of the white's king in the <a href="keyword://chess-notation">chess notation</a>.</p>
</li>
<li>
<p><strong>[input] string amazon</strong></p>
<p>Position of the white's <em>amazon</em> in the same notation.</p>
<p><em>Guaranteed constraints:</em><br>
<code>amazon ≠ king</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array of four integers, each equal to the number of black's king positions corresponding to a specific situation. The integers should be presented in the same order as the situations were described, i.e. <code>0</code> for checkmates, <code>1</code> for checks, etc.</p>
</li>
</ul>
</div>