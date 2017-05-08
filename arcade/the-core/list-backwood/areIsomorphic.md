<div class="markdown"><p>Two two-dimensional arrays are <em>isomorphic</em> if they have the same number of rows and each pair of respective rows contains the same number of elements.</p>
<p>Given two two-dimensional arrays, check if they are isomorphic.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>array1 = [[1, 1, 1],
          [0, 0]]
</code></pre>
<p>and</p>
<pre><code>array2 = [[2, 1, 1],
          [2, 1]]
</code></pre>
<p>the output should be<br>
<code>areIsomorphic(array1, array2) = true</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>array1 = [[2],
          []]
</code></pre>
<p>and</p>
<pre><code>array2 = [[2]]
</code></pre>
<p>the output should be<br>
<code>areIsomorphic(array1, array2) = false</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer array1</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ array1.length ≤ 5</code>,<br>
<code>0 ≤ array1[i].length ≤ 5</code>,<br>
<code>0 ≤ array1[i][j] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer array2</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ array2.length ≤ 5</code>,<br>
<code>0 ≤ array2[i].length ≤ 5</code>,<br>
<code>0 ≤ array2[i][j] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>