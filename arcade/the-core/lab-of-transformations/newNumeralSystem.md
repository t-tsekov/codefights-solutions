<div class="markdown"><p>Your Informatics teacher at school likes coming up with new ways to help you understand the material. When you started studying numeral systems, he introduced his own numeral system, which he's convinced will help clarify things. His numeral system has base <code>26</code>, and its digits are represented by English capital letters - <code>A</code> for <code>0</code>, <code>B</code> for <code>1</code>, and so on.</p>
<p>The teacher assigned you the following numeral system exercise: given a one-digit <code>number</code>, you should find all unordered pairs of one-digit numbers whose values add up to the <code>number</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>number = 'G'</code>, the output should be<br>
<code>newNumeralSystem(number) = ["A + G", "B + F", "C + E", "D + D"]</code>.</p>
<p>Translating this into the decimal numeral system we get: <code>number = 6</code>, so it is <code>["0 + 6", "1 + 5", "2 + 4", "3 + 3"]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] char number</strong></p>
<p>A character representing a correct one-digit number in the new numeral system.</p>
<p><em>Guaranteed constraints:</em><br>
<code>'A' ≤ number ≤ 'Z'</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>An array of strings in the format <code>"letter1 + letter2"</code>, where <code>"letter1"</code> and <code>"letter2"</code> are correct one-digit numbers in the new numeral system. The strings should be sorted by <code>"letter1"</code>.</p>
<p><em>Note</em> that <code>"letter1 + letter2"</code> and <code>"letter2 + letter1"</code> are equal pairs and we don't consider them to be different.</p>
</li>
</ul>
</div>