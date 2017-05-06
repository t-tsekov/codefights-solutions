<div class="markdown"><p>You're given two integers, <code>n</code> and <code>m</code>. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.</p>
<p>Return the value of <code>2<sup>position_of_the_found_bit</sup></code> (0-based).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 11</code> and <code>m = 13</code>, the output should be<br>
<code>differentRightmostBit(n, m) = 2</code>.</p>
<p><code>11<sub>10</sub> = 10<b><font color="red">1</font></b>1<sub>2</sub></code>, <code>13<sub>10</sub> = 11<b><font color="red">0</font></b>1<sub>2</sub></code>, the rightmost bit in which they differ is the bit at position <code>1</code> (0-based) from the right in the binary representations.<br>
So the answer is <code>2<sup>1</sup> = 2</code>.</p>
</li>
<li>
<p>For <code>n = 7</code> and <code>m = 23</code>, the output should be<br>
<code>differentRightmostBit(n, m) = 16</code>.</p>
<p><code>7<sub>10</sub> = 111<sub>2</sub></code>, <code>23<sub>10</sub> = 10111<sub>2</sub></code>, i.e.</p>
<pre><code>00111
10111
</code></pre>
<p>So the answer is <code>2<sup>4</sup> = 16</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ n ≤ 2<sup>30</sup></code>.</p>
</li>
</ul>
<ul>
<li>
<p><strong>[input] integer m</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ m ≤ 2<sup>30</sup></code>,<br>
<code>n ≠ m.</code></p>
</li>
</ul>
<ul>
<li><strong>[output] integer</strong></li>
</ul>
</div>