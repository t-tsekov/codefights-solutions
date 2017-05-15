<div class="markdown"><p>All DNA is composed of a series of nucleotides abbreviated as <code>A</code>, <code>C</code>, <code>G</code>, and <code>T</code>. In research, it can be useful to identify repeated sequences within DNA.</p>
<p>Write a function to find all the 10-letter sequences (substrings) that occur more than once in a DNA molecule <code>s</code>, and return them in <a href="keyword://lexicographical-order-for-strings">lexicographical order</a>. These sequences can overlap.</p>
<p><strong>Example</strong></p>
<p>For <code>s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"</code>, the output should be<br>
<code>repeatedDNASequences(s) = ["AAAAACCCCC", "CCCCCAAAAA"]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ s.length ≤ 5000</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>An array containing all of the potential 10-letter sequences that occur more than once in <code>s</code>.</p>
</li>
</ul>
</div>