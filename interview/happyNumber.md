<div class="markdown"><p>A <em>happy number</em> is a number defined by the following process: Start with any positive integer and replace the number with the sum of the squares of its digits. Repeat this process until the number equals <code>1</code>, at which point it will stay <code>1</code>, or it loops endlessly in a cycle that does not include <code>1</code>. A number for which this process ends in <code>1</code> is <em>happy</em>.</p>
<p>Write an algorithm to determine whether or not a number is <em>happy</em>.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 19</code>, the output should be<br>
<code>happyNumber(n) = true</code>.</p>
<p>Following the process outlined above:<br>
* 1<sup>2</sup> + 9<sup>2</sup> = 82;<br>
* 8<sup>2</sup> + 2<sup>2</sup> = 68;<br>
* 6<sup>2</sup> + 8<sup>2</sup> = 100;<br>
* 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if the number is <em>happy</em>, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>