<div class="markdown"><p>The numeric system represented by <a href="https://en.wikipedia.org/wiki/Roman_numerals">Roman numerals</a> originated in ancient Rome. Numbers in this system are represented by combinations of letters from the Latin alphabet. Roman numerals, as we use them today, are based on seven symbols:</p>
<p><code>I:1; V:5; X:10; L:50; C:100; D:500; M: 1,000</code></p>
<p>You have a string <code>s</code> that represents a number written as a Roman numeral. If the string <code>s</code> is a correctly written Roman numeral, return this number as an integer. If <code>s</code> isn't a correctly written Roman numeral, return <code>-1</code>.</p>
<p>For this challenge, assume that there is no restriction on the maximum number that can be written in Roman numerals.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>s = "MMXV"</code>, the output should be<br>
<code>integerValueOfRomanNumeral(s) = 2015</code>;</p>
</li>
<li>
<p>For <code>s = "XLX"</code>, the output should be<br>
<code>integerValueOfRomanNumeral(s) = -1</code>.</p>
<p><code>XL</code> is a valid Roman numeral representing <code>40</code>, but <code>XLX</code> is not valid.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string <code>s</code> consisting of characters <code>I, V, X, L, C, D, M</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The integer value of the given Roman numeral, or <code>-1</code> if the input doesn't contain a correct Roman numeral.</p>
</li>
</ul>
</div>