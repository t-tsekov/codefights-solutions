<div class="markdown"><p>Given a string, check if it can become a <a href="keyword://palindrome">palindrome</a> through a case change of some (possibly, none) letters.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>inputString = "AaBaa"</code>, the output should be<br>
<code>isCaseInsensitivePalindrome(inputString) = true</code>.</p>
<p><code>"aabaa"</code> is a palindrome as well as <code>"AABAA"</code>, <code>"aaBaa"</code>, etc.</p>
</li>
<li>
<p>For <code>inputString = "abac"</code>, the output should be<br>
<code>isCaseInsensitivePalindrome(inputString) = false</code>.</p>
<p>All the strings which can be obtained via changing case of some group of letters, i.e. <code>"abac"</code>, <code>"Abac"</code>, <code>"aBAc"</code> and 13 more, are not palindromes.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string inputString</strong></p>
<p>Non-empty string consisting of letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>4 ≤ inputString.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>