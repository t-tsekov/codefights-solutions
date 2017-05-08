<div class="markdown"><p>Given a rectangular matrix and an integer <code>column</code>, return an array containing the elements of the <code>column<sup>th</sup></code> column of the given matrix (the leftmost column is the <code>0<sup>th</sup></code> one).</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[1, 1, 1, 2], 
          [0, 5, 0, 4], 
          [2, 1, 3, 6]]
</code></pre>
<p>and <code>column = 2</code>, the output should be<br>
<code>extractMatrixColumn(matrix, column) = [1, 0, 3]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>2-dimensional array of integers representing a rectangular matrix.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ matrix.length ≤ 4</code>,<br>
<code>1 ≤ matrix[0].length ≤ 4</code>,<br>
<code>0 ≤ matrix[i][j] ≤ 300</code>.</p>
</li>
<li>
<p><strong>[input] integer column</strong></p>
<p>An integer not greater than the number of <code>matrix</code> columns.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ column ≤ matrix[i].length - 1</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
</div>