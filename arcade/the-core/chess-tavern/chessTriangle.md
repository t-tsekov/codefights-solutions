<div class="markdown"><p>Consider a bishop, a knight and a rook on an <code>n × m</code> chessboard. They are said to form a <em>triangle</em> if each piece attacks exactly one other piece and is attacked by exactly one piece. Calculate the number of ways to choose positions of the pieces to form a <em>triangle</em>.</p>
<p>Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from its position.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/chessTriangle/img/moves.png?_tm=1490625690642" alt=""></p>
<p><strong>Example</strong></p>
<p>For <code>n = 2</code> and <code>m = 3</code>, the output should be<br>
<code>chessTriangle(n, m) = 8</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/chessTriangle/img/combinations.png?_tm=1490625690826" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 40</code>.</p>
</li>
<li>
<p><strong>[input] integer m</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ m ≤ 40</code>,<br>
<code>3 ≤ n · m</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>