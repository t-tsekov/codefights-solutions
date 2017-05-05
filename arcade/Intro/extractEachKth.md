<div class="markdown"><p>Given array of integers, remove each <code>k<sup>th</sup></code> element from it.</p>
<p><strong>Example</strong></p>
<p>For <code>inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code> and <code>k = 3</code>, the output should be<br>
<code>extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer inputArray</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ inputArray.length ≤ 15</code>,<br>
<code>-20 ≤ inputArray[i] ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p><code>inputArray</code> without elements <code>k - 1</code>, <code>2k - 1</code>, <code>3k - 1</code> etc.</p>
</li>
</ul>
</div>