<div class="markdown"><p>Consider the following ciphering algorithm:</p>
<ul>
<li>For each character replace it with its code.</li>
<li>Concatenate all of the obtained numbers.</li>
</ul>
<p>Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.</p>
<p><strong>Note:</strong> here the <em>character's code</em> means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.</p>
<p><strong>Example</strong></p>
<p>For <code>cipher = "10197115121"</code>, the output should be<br>
<code>decipher(cipher) = "easy"</code>.</p>
<p>Explanation: <code>charCode('e') = 101</code>, <code>charCode('a') = 97</code>, <code>charCode('s') = 115</code> and <code>charCode('y') = 121</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string cipher</strong></p>
<p>A non-empty string which is guaranteed to be a cipher for some other string of lowercase letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ cipher.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
</div>