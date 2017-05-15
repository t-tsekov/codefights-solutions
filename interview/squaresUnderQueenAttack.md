<div class="markdown"><p><em>Note: Write a solution with <code>O(queries.length + queens.length + n)</code> complexity and <code>O(n)</code> additional memory, since this is what you would be asked to do during a real interview.</em></p>
<p>In chess, queens can move any number of squares vertically, horizontally, or diagonally. You have an <code>n × n</code> chessboard with some <code>queens</code> on it. You are given several <code>queries</code>, each of which represents one square on the chessboard. For each query square, determine whether it can be attacked by a queen or not.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 5</code>, <code>queens = [[1, 1], [3, 2]]</code> and <code>queries = [[1, 1], [0, 3], [0, 4], [3, 4], [2, 0], [4, 3], [4, 0]]</code>, the output should be<br>
<code>squaresUnderQueenAttack(n, queens, queries) = [true, false, false, true, true, true, false]</code>.</p>
<p>Here are the squares on this chessboard that can be attacked by a queen:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/squaresUnderQueenAttack/img/example.png?_tm=1491302363066" alt=""></p>
<p>Only squares <code>(0, 3)</code>, <code>(0, 4)</code>, <code>(2, 4)</code>, and <code>(4, 0)</code> are not under attack.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>The size of the chessboard.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer queens</strong></p>
<p>The placement of all queens on the chessboard. For each valid <code>i</code>, <code>queens[i]</code> contains exactly two elements indicating the coordinates of the <code>i<sup>th</sup></code> queen (0-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ queens.length ≤ 10<sup>6</sup></code>,<br>
<code>queens[i].length = 2</code>,<br>
<code>0 ≤ queens[i][j] ≤ n - 1</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer queries</strong></p>
<p>The queries. For each valid <code>i</code>, <code>queries[i]</code> contains exactly two elements indicating the coordinates of the <code>i<sup>th</sup></code> query square (0-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ queries.length ≤ 10<sup>3</sup></code>,<br>
<code>queries[i].length = 2</code>,<br>
<code>0 ≤ queries[i][j] ≤ n - 1</code>.</p>
</li>
<li>
<p><strong>[output] array.boolean</strong></p>
<p>For <code>i<sup>th</sup></code> query, return <code>true</code> if this square can be attacked by a queen and <code>false</code> otherwise.</p>
</li>
</ul>
</div>