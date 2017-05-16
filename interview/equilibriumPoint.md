<div class="markdown"><p>Equilibrium position in an array is a position at which the sum of elements before it is equal to the sum of elements after it. Given an array <code>arr</code>, your task is to determine at which position equilibrium first occurs in the array. If there is no equilibrium position, the answer should be <code>-1</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>arr = [5]</code>, the output should be<br><br>
<code>equilibriumPoint(arr) = 1</code>.</p>
<p>Explanation: Since this array only has one element, the equilibrium point is at position <code>1</code>.</p>
</li>
<li>
<p>For <code>arr = [10, 5, 3, 5, 2, 2, 6, 8]</code>, the output should be<br><br>
<code>equilibriumPoint(arr) = 4</code>.</p>
<p>Explanation: The equilibrium point is at position <code>4</code>, because the sum of elements before it - <code>(10 + 5 + 3)</code> - is equal to the sum of elements after it - <code>(2 + 2 + 6 + 8)</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer arr</strong></p>
<p><em>Guaranteed constraints:</em><br><br>
<code>1 ≤ arr.length ≤ 10<sup>5</sup></code>,<br><br>
<code>-1000 ≤ arr[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The first equilibrium position in <code>arr</code>, or <code>-1</code>.</p>
</li>
</ul>
</div>