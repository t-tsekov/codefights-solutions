<div class="markdown"><p>In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the <em>same diagonal</em>, they immediately rush towards the opposite ends of that same diagonal.</p>
<p>Given the initial positions (in chess notation) of two bishops, <code>bishop1</code> and <code>bishop2</code>, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>bishop1 = "d7"</code> and <code>bishop2 = "f5"</code>, the output should be<br>
<code>bishopDiagonal(bishop1, bishop2) = ["c8", "h3"]</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_1.jpg?_tm=1486560044782" alt=""></p>
</li>
<li>
<p>For <code>bishop1 = "d8"</code> and <code>bishop2 = "b5"</code>, the output should be<br>
<code>bishopDiagonal(bishop1, bishop2) = ["b5", "d8"]</code>.</p>
<p>The bishops don't belong to the same diagonal, so they don't move.<br>
<img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_2.jpg?_tm=1486560045546" alt=""></p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string bishop1</strong></p>
<p>Coordinates of the first bishop in <a href="keyword://chess-notation">chess notation</a>.</p>
</li>
<li>
<p><strong>[input] string bishop2</strong></p>
<p>Coordinates of the second bishop in the same notation.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Coordinates of the bishops in <a href="keyword://lexicographical-order-for-strings">lexicographical order</a> after they check the diagonals they stand on.</p>
</li>
</ul>
</div>