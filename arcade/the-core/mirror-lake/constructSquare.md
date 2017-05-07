<div class="markdown"><p>Given a string consisting of lowercase English letters, find the largest square number which can be obtained by <em>reordering</em> the string's characters and <em>replacing</em> them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.</p>
<p>If there is no solution, return <code>-1</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>s = "ab"</code>, the output should be<br>
<code>constructSquare(s) = 81</code>.<br>
The largest <code>2</code>-digit square number with different digits is <code>81</code>.</li>
<li>For <code>s = "zzz"</code>, the output should be<br>
<code>constructSquare(s) = -1</code>.<br>
There are no <code>3</code>-digit square numbers with identical digits.</li>
<li>For <code>s = "aba"</code>, the output should be<br>
<code>constructSquare(s) = 900</code>.<br>
It can be obtained after reordering the initial string into <code>"baa"</code> and replacing "a" with <code>0</code> and "b" with <code>9</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length &lt; 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>