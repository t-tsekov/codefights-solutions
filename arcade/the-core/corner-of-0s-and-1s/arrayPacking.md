<div class="markdown"><p>You are given an array of up to four non-negative integers, each less than <code>256</code>.</p>
<p>Your task is to pack these integers into one number <code>M</code> in the following way:</p>
<ul>
<li>The first element of the array occupies the first <code>8</code> bits of <code>M</code>;</li>
<li>The second element occupies next <code>8</code> bits, and so on.</li>
</ul>
<p>Return the obtained integer <code>M</code>.</p>
<p><u>Note:</u> the phrase <em>"first bits of <code>M</code>"</em> refers to the <em>least significant bits</em> of <code>M</code> - the right-most bits of an integer. For further clarification see the following example.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [24, 85, 0]</code>, the output should be<br>
<code>arrayPacking(a) = 21784</code>.</p>
<p>An array <code>[24, 85, 0]</code> looks like <code>[00011000, 01010101, 00000000]</code> in binary.<br>
After packing these into one number we get <code>00000000 01010101 00011000</code> (spaces are placed for convenience), which equals to <code>21784</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ a.length ≤ 4</code>,<br>
<code>0 ≤ a[i] &lt; 256</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>