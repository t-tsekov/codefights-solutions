<div class="markdown"><p>You are given an array of integers <code>arr</code>. <em>Range sum query</em> is defined by a pair of non-negative integers <code>L</code> and <code>R</code> (<code>L ≤ R</code>). An output to a <em>range sum query</em> on the given array is the sum of all elements of <code>arr</code> with indices from <code>L</code> to <code>R</code> inclusive.</p>
<p>Find an algorithm that given a list of range sum queries can rearrange the array <code>arr</code> in such a way that the total sum of all of the query outputs is maximized.</p>
<p><strong>Example</strong></p>
<p>For <code>arr = [2, 1, 2]</code> and <code>queries = [[0, 1]]</code>, the output should be<br>
<code>maximumSum(arr, queries) = 4</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer arr</strong></p>
<p>An initial array.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ arr.length ≤ 10</code>,<br>
<code>1 ≤ arr[i] ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer queries</strong></p>
<p>Array of <em>range sum queries</em>, each query is an array of two non-negative integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ queries.length ≤ 10</code>,<br>
<code>0 ≤ queries[i][0] ≤ queries[i][1] &lt; arr.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>Maximum possible total sum of the given range sum query outputs.</p>
</li>
</ul>
</div>