<div class="markdown"><p>You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?</p>
<p>It is guaranteed that the sum of all elements in the array is divisible by <code>3</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [0, -1, 0, -1, 0, -1]</code>, the output should be<br>
<code>threeSplit(a) = 4</code>.</p>
<p>Here are all possible ways:</p>
<ul>
<li><code>[0, -1] [0, -1] [0, -1]</code></li>
<li><code>[0, -1] [0, -1, 0] [-1]</code></li>
<li><code>[0, -1, 0] [-1, 0] [-1]</code></li>
<li><code>[0, -1, 0] [-1] [0, -1]</code></li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ a.length ≤ 10<sup>4</sup></code>,<br>
<code>-10<sup>8</sup> ≤ a[i] ≤ 10<sup>8</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>It's guaranteed that for the given test cases the answer always fits signed <code>32</code>-bit integer type.</p>
</li>
</ul>
</div>