<div class="markdown"><p>There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of <a href="keyword://prefix-sums">prefix sums</a>. Given array <code>a</code>, your task is to calculate all its prefix sums.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [1, 2, 3]</code>, the output should be<br>
<code>prefSum(a) = [1, 3, 6]</code>.</p>
<p>Here's how the <em>prefix sums</em> can be calculated: <code>[1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ a.length ≤ 3 · 10<sup>4</sup></code>,<br>
<code>-1000 ≤ a[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
</div>