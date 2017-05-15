<div class="markdown"><p>The string <code>s</code> contains dashes that split it into groups of characters. You are given an integer <code>k</code> that represents the number of characters in groups that your output should have. Your goal is to return a new string that breaks <code>s</code> into groups with a length of <code>k</code> by placing dashes at the correct intervals. If necessary, the first group of characters can be shorter than <code>k</code>. It is guaranteed that there are no consecutive dashes in <code>s</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>s = "2-4a0r7-4k"</code> and <code>k = 4</code>, the output should be<br>
<code>stringReformatting(s, k) = "24a0-r74k"</code>;</p>
<p>The input string <code>"2-4a0r7-4k"</code> is split into three groups with lengths of <code>1</code>, <code>5</code> and <code>2</code>. Since <code>k = 4</code>, you need to split the string into two groups of <code>4</code> characters each, making the output string <code>"24A0-R74k"</code>.</p>
</li>
<li>
<p>For <code>s = "2-4a0r7-4k"</code> and <code>k = 3</code>, the output should be<br>
<code>stringReformatting(s, k) = "24-a0r-74k"</code>.</p>
<p>Given the same input string and <code>k = 3</code>, split the string into groups of <code>2</code>, <code>3</code>, and <code>3</code> characters to get the output string of <code>"24-a0r-74k"</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string containing some dashes.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ s.length</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string, reformatted so that dashes divide it into groups with a length of <code>k</code> or shorter.</p>
</li>
</ul>
</div>