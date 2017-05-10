<div class="markdown"><p>It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write a code, you expect the result of the modulus operator to always be an integer, but thanks to Python it's not necessarily true.</p>
<p>To fix this, you decided to write your own modulus operator as a function. Your task is to implement a function that, given a number <code>n</code>, returns <code>-1</code> if this number is not an integer and <code>n % 2</code> otherwise. It is guaranteed that if the number represents an integer, it will be written without decimal point.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 15</code>, the output should be<br>
<code>modulus(n) = 1</code>;</p>
</li>
<li>
<p>For <code>n = 23.12</code>, the output should be<br>
<code>modulus(n) = -1</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] numeric n</strong></p>
<p>A non-negative number that can be an <code>int</code>, a <code>float</code> or a <code>long</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ n ≤ 1000</code></p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p><code>n % 2</code> if <code>n</code> is an integer, <code>-1</code> otherwise.</p>
</li>
</ul>
</div>
