<div class="markdown"><p>Given a sorted array of integers <code>a</code>, find such an integer <code>x</code> that the value of</p>
<pre><code>abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
</code></pre>
<p>is the <em>smallest possible</em> (here <code>abs</code> denotes the absolute value).<br>
If there are several possible answers, output the <em>smallest</em> one.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [2, 4, 7]</code>, the output should be<br>
<code>absoluteValuesSumMinimization(a) = 4</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>A non-empty array of integers, sorted in ascending order.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ a.length ≤ 200</code>,<br>
<code>-10<sup>6</sup> ≤ a[i] ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>