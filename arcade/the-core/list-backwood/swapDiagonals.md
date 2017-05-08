<div class="markdown"><p>The <em>longest diagonals</em> of a square matrix are defined as follows:</p>
<ul>
<li>the first <em>longest diagonal</em> goes from the top left corner to the bottom right one;</li>
<li>the second <em>longest diagonal</em> goes from the top right corner to the bottom left one.</li>
</ul>
<p>Given a square <code>matrix</code>, your task is to swap its <em>longest diagonals</em> by exchanging their elements at the corresponding positions.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
</code></pre>
<p>the output should be</p>
<pre><code>swapDiagonals(matrix) = [[3, 2, 1],
                         [4, 5, 6],
                         [9, 8, 7]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ matrix.length ≤ 10</code>,<br>
<code>matrix.length = matrix[i].length</code>,<br>
<code>1 ≤ matrix[i][j] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>Matrix with swapped diagonals.</p>
</li>
</ul>
</div>