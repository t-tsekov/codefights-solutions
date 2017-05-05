<div class="markdown"><p>Given the positions of a white <code>bishop</code> and a black <code>pawn</code> on the standard chess board, determine whether the bishop can capture the pawn in one move.</p>
<p>The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:<br>
<img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/bishop.jpg?_tm=1493360096740" alt=""></p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>bishop = "a1"</code> and <code>pawn = "c3"</code>, the output should be<br>
<code>bishopAndPawn(bishop, pawn) = true</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/ex1.jpg?_tm=1493360096945" alt=""></p>
</li>
<li>
<p>For <code>bishop = "h1"</code> and <code>pawn = "h3"</code>, the output should be<br>
<code>bishopAndPawn(bishop, pawn) = false</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/ex2.jpg?_tm=1493360097459" alt=""></p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string bishop</strong></p>
<p>Coordinates of the white bishop in the <a href="keyword://chess-notation">chess notation</a>.</p>
</li>
<li>
<p><strong>[input] string pawn</strong></p>
<p>Coordinates of the black pawn in the same notation.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the bishop can capture the pawn, <code>false</code> otherwise.</p>
</li>
</ul>
</div>