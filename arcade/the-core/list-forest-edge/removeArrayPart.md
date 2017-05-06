<div class="markdown"><p>Remove a part of a given array between given 0-based indexes <code>l</code> and <code>r</code> (inclusive).</p>
<p><strong>Example</strong></p>
<p>For <code>inputArray = [2, 3, 2, 3, 4, 5]</code>, <code>l = 2</code> and <code>r = 4</code>, the output should be<br>
<code>removeArrayPart(inputArray, l, r) = [2, 3, 5]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer inputArray</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ inputArray.length ≤ 10</code>,<br>
<code>-10 ≤ inputArray[i] ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer l</strong></p>
<p>Left index of the part to be removed (0-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ l ≤ r</code>.</p>
</li>
<li>
<p><strong>[input] integer r</strong></p>
<p>Right index of the part to be removed (0-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>l ≤ r &lt; inputArray.length</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
</div>