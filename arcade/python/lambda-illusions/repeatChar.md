<div class="markdown"><p>To make debug output more understandable, you often separate sets of logs by a single line of the same character. Since you use this method very often, you'd like to write a function that would handle printing the separator.</p>
<p>Implement a function that, given a character <code>ch</code> and the number of times it should be repeated <code>n</code>, returns a string of <code>n</code> characters <code>ch</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>ch = '*'</code> and <code>n = 20</code>, the output should be<br>
<code>repeatChar(ch, n) = "********************"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] char ch</strong></p>
<p>The character that should be repeated.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of times the given character should be repeated.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string consisting of <code>n</code> characters <code>ch</code>.</p>
</li>
</ul>
</div>