<div class="markdown"><p>Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[2, 7, 1], 
          [0, 2, 0], 
          [1, 3, 1]]
</code></pre>
<p>the output should be<br>
<code>rowsRearranging(matrix) = false</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[6, 4], 
          [2, 2], 
          [4, 3]]
</code></pre>
<p>the output should be<br>
<code>rowsRearranging(matrix) = true</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>A 2-dimensional array of integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ matrix.length ≤ 10</code>,<br>
<code>1 ≤ matrix[0].length ≤ 10</code>,<br>
<code>-300 ≤ matrix[i][j] ≤ 300</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>