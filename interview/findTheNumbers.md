<div class="markdown"><p><em>Try to solve this challenge with linear complexity and using <code>O(1)</code> additional memory, since this is what you would be asked to do during a real interview.</em></p>
<p>You have an array <code>a</code> containing <code>2 * n + 2</code> positive numbers, in which <code>n</code> numbers occur twice and two other numbers occur only once and are distinct. Find the two distinct numbers and return them in ascending order.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>a = [1, 3, 5, 6, 1, 4, 3, 6]</code>, the output should be<br>
<code>findTheNumbers(a) = [4, 5]</code>;</li>
<li>For <code>a = [4, 5, 6, 5, 3, 4]</code>, the output should be<br>
<code>findTheNumbers(a) = [3, 6]</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>An array that contains <code>2 * n + 2</code> positive integers.</p>
<p><em>Guaranteed constraints:</em><br><br>
<code>2 ≤ a.length ≤ 10<sup>5</sup>,<br><br>
<code>a.length</code> is even,<br><br>
<code>1 ≤ a[i] ≤ 10<sup>9</sup></code>.</code></p><code>
</code></li><code>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Two non-repeated elements in ascending order.</p>
</li>
</code></ul><code>
</code></div>