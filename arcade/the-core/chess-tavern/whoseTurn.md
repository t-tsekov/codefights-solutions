<div class="markdown"><p>Imagine a standard chess board with only two white and two black knights placed in their standard starting positions: the white knights on <code>b1</code> and <code>g1</code>; the black knights on <code>b8</code> and <code>g8</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/whoseTurn/img/initial_pos.png?_tm=1486563349466" alt=""></p>
<p>There are two players: one plays for white, the other for black. During each move, the player picks one of his knights and moves it to an unoccupied square according to standard chess rules. Thus, a knight on <code>d5</code> can move to any of the following squares: <code>b6</code>, <code>c7</code>, <code>e7</code>, <code>f6</code>, <code>f4</code>, <code>e3</code>, <code>c3</code>, and <code>b4</code>, as long as it is not occupied by either a friendly or an enemy knight.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/whoseTurn/img/knight.jpg?_tm=1486563349764" alt=""></p>
<p>The players take turns in making moves, starting with the white player. Given the configuration <code>p</code> of the knights after an unspecified number of moves, determine whose turn it is.</p>
<p><strong>Example</strong></p>
<p>For <code>p = "b1;g1;b8;g8"</code>, the output should be<br>
<code>whoseTurn(p) = true</code>.</p>
<p>The configuration corresponds to the initial state of the game. Thus, it's white's turn.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string p</strong></p>
<p>The positions of the four knights, starting with white knights, separated by a semicolon, in the <a href="keyword://chess-notation">chess notation</a>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if white is to move, <code>false</code> otherwise.</p>
</li>
</ul>
</div>