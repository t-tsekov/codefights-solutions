<div class="markdown"><p>Let's call <code>product(x)</code> the product of <code>x</code>'s digits. Given an array of integers <code>a</code>, calculate <code>product(x)</code> for each <code>x</code> in <code>a</code>, and return the number of distinct results you get.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [2, 8, 121, 42, 222, 23]</code>, the output should be<br>
<code>uniqueDigitProducts(a) = 3</code>.</p>
<p>Here are the products of the array's elements:</p>
<ul>
<li><code>2</code>: <code>product(2) = 2</code>;</li>
<li><code>8</code>: <code>product(8) = 8</code>;</li>
<li><code>121</code>: <code>product(121) = 1 * 2 * 1 = 2</code>;</li>
<li><code>42</code>: <code>product(42) = 4 * 2 = 8</code>;</li>
<li><code>222</code>: <code>product(222) = 2 * 2 * 2 = 8</code>;</li>
<li><code>23</code>: <code>product(23) = 2 * 3 = 6</code>.</li>
</ul>
<p>As you can see, there are only <code>3</code> different products: <code>2</code>, <code>6</code> and <code>8</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ a.length ≤ 10<sup>5</sup></code>,<br>
<code>1 ≤ a[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of different digit products in <code>a</code>.</p>
</li>
</ul>
</div>