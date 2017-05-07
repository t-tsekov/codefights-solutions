<div class="markdown"><p>A <em>ciphertext alphabet</em> is obtained from the <a href="keyword://plaintext-alphabet">plaintext alphabet</a> by means of rearranging some characters. For example <code>"bacdef...xyz"</code> will be a simple ciphertext alphabet where <code>a</code> and <code>b</code> are rearranged.</p>
<p>A <em>substitution cipher</em> is a method of encoding where each letter of the <em>plaintext alphabet</em> is replaced with the corresponding (i.e. having the same index) letter of some <em>ciphertext alphabet</em>.</p>
<p>Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) <em>substitution ciphers</em>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>string1 = "aacb"</code> and <code>string2 = "aabc"</code>, the output should be<br>
<code>isSubstitutionCipher(string1, string2) = true</code>.</p>
<p>Any <em>ciphertext alphabet</em> that starts with <code>acb...</code> would make this transformation possible.</p>
</li>
<li>
<p>For <code>string1 = "aa"</code> and <code>string2 = "bc"</code>, the output should be<br>
<code>isSubstitutionCipher(string1, string2) = false</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string string1</strong></p>
<p>A string consisting of lowercase characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ string1.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string string2</strong></p>
<p>A string consisting of lowercase characters of the same length as <code>string1</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>string2.length = string1.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>