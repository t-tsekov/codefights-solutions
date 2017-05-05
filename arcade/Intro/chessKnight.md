<div class="markdown"><p>Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.</p>
<p>The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/knight.jpg?_tm=1486560102464" alt=""></p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>cell = "a1"</code>, the output should be<br>
<code>chessKnight(cell) = 2</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/ex_1.jpg?_tm=1486560102718" alt=""></p>
</li>
<li>
<p>For <code>cell = "c2"</code>, the output should be<br>
<code>chessKnight(cell) = 6</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/chessKnight/img/ex_2.jpg?_tm=1486560102902" alt=""></p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string cell</strong></p>
<p>String consisting of 2 letters - coordinates of the knight on an <code>8 × 8</code> chessboard in <a href="keyword://chess-notation">chess notation</a>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>