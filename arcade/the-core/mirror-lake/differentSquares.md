<div class="markdown"><p>Given a rectangular matrix containing only digits, calculate the number of different <code>2 × 2</code> squares in it.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
</code></pre>
<p>the output should be<br>
<code>differentSquares(matrix) = 6</code>.</p>
<p>Here are all <code>6</code> different <code>2 × 2</code> squares:</p>
<ul>
<li>1 2<br>
2 2</li>
<li>2 1<br>
2 2</li>
<li>2 2<br>
2 2</li>
<li>2 2<br>
1 2</li>
<li>2 2<br>
2 3</li>
<li>2 3<br>
2 1</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ matrix.length ≤ 100</code>,<br>
<code>1 ≤ matrix[i].length ≤ 100</code>,<br>
<code>0 ≤ matrix[i][j] ≤ 9</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of different <code>2 × 2</code> squares in <code>matrix</code>.</p>
</li>
</ul>
</div>