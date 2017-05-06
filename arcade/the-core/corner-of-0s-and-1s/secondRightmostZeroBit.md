<div class="markdown"><p>Presented with the integer <code>n</code>, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.</p>
<p>Return the value of <code>2<sup>position_of_the_found_bit</sup></code>.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 37</code>, the output should be<br>
<code>secondRightmostZeroBit(n) = 8</code>.</p>
<p><code>37<sub>10</sub> = 10<b><font color="red">0</font></b>101<sub>2</sub></code>. The second rightmost zero bit is at position <code>3</code> (0-based) from the right in the binary representation of <code>n</code>.<br>
Thus, the answer is <code>2<sup>3</sup> = 8</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>4 ≤ n ≤ 2<sup>30</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>