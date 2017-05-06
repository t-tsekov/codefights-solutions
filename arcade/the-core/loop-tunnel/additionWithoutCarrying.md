<div class="markdown"><p>A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.</p>
<p>Given two integers, find the result which the little boy will get.</p>
<p><em>Note: the boy used <a href="https://www.mathsisfun.com/numbers/addition-column.html">this</a> site as the source of knowledge, feel free to check it out too if you are not familiar with column addition</em>.</p>
<p><strong>Example</strong></p>
<p>For <code>param1 = 456</code> and <code>param2 = 1734</code>, the output should be<br>
<code>additionWithoutCarrying(param1, param2) = 1180</code>.</p>
<pre><code>   456
  1734
+ ____
  1180
</code></pre>
<p>The little boy goes from right to left:</p>
<ul>
<li><code>6 + 4 = 10</code> but the little boy forgets about <code>1</code> and just writes down <code>0</code> in the last column</li>
<li><code>5 + 3 = 8</code></li>
<li><code>4 + 7 = 11</code> but the little boy forgets about the leading <code>1</code> and just writes down <code>1</code> under <code>4</code> and <code>7</code>.</li>
<li>There is no digit in the first number corresponding to the leading digit of the second one, so the little boy imagines that <code>0</code> is written before <code>456</code>. Thus, he gets <code>0 + 1 = 1</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer param1</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ param1 ≤ 99999</code>.</p>
</li>
<li>
<p><strong>[input] integer param2</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ param2 ≤ 59999</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The result that the little boy will get.</p>
</li>
</ul>
</div>