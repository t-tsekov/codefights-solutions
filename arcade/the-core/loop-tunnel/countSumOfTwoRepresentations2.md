<div class="markdown"><p>Given integers <code>n</code>, <code>l</code> and <code>r</code>, find the number of ways to represent <code>n</code> as a sum of two integers <code>A</code> and <code>B</code> such that <code>l ≤ A ≤ B ≤ r</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 6</code>, <code>l = 2</code> and <code>r = 4</code>, the output should be<br>
<code>countSumOfTwoRepresentations2(n, l, r) = 2</code>.</p>
<p>There are just two ways to write <code>6</code> as <code>A + B</code>, where <code>2 ≤ A ≤ B ≤ 4</code>: <code>6 = 2 + 4</code> and <code>6 = 3 + 3</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ n ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer l</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ l ≤ r</code>.</p>
</li>
<li>
<p><strong>[input] integer r</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>l ≤ r ≤ 10<sup>9</sup></code>,<br>
<code>r - l ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>