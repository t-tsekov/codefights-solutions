<div class="markdown"><p>Given array of integers, for each position <code>i</code>, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position <code>i</code> in the answer. If no such value can be found, store <code>-1</code> instead.</p>
<p><strong>Example</strong></p>
<p>For <code>items = [3, 5, 2, 4, 5]</code>, the output should be<br>
<code>arrayPreviousLess(items) = [-1, 3, -1, 2, 4]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer items</strong></p>
<p>Non-empty array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ items.length ≤ 15</code>,<br>
<code>1 ≤ items[i] ≤ 200</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array containing answer values computed as described above.</p>
</li>
</ul>
</div>