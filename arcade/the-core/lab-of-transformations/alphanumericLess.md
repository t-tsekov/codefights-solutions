<div class="markdown"><p>An <em>alphanumeric</em> ordering of strings is defined as follows: each string is considered as a sequence of tokens, where each token is a letter or a number (as opposed to an isolated digit, as is the case of lexicographic ordering). For example, the tokens of a string <code>"ab01c004"</code> are <code>[a, b, 01, c, 004]</code>. In order to compare two strings, you break them down into tokens and compare corresponding pairs of tokens with each other (i.e. first token of the first string, with the first token of the second string etc).</p>
<p>Here is how tokens are compared:</p>
<ul>
<li>If a letter is compared with another letter, the usual order applies.</li>
<li>A number is always <em>less</em> than a letter.</li>
<li>When two numbers are compared, their values are compared. Leading zeros, if any, are ignored.</li>
</ul>
<p>If at some point one string has no more tokens left while the other one still does, the one with fewer tokens is considered <em>smaller</em>.</p>
<p>If the two strings <code>s1</code> and <code>s2</code> appear to be equal, consider the smallest index <code>i</code> such that <code>tokens(s1)[i]</code> and <code>tokens(s2)[i]</code> (where <code>tokens(s)[i]</code> is the <code>i<sup>th</sup></code> token of string <code>s</code>) differ only by the number of leading zeros. If no such <code>i</code> exists, the strings are indeed equal. Otherwise, the string whose <code>i<sup>th</sup></code> token has more leading zeros is considered less.</p>
<p>Here are some examples of comparing strings using alphanumeric ordering.</p>
<pre><code>"a" &lt; "a1" &lt; "ab"
"ab42" &lt; "ab000144" &lt; "ab00144" &lt; "ab144" &lt; "ab000144x"
"x11y012" &lt; "x011y13"
</code></pre>
<p><strong>Example</strong></p>
<ul>
<li>For <code>s1 = "a"</code> and <code>s2 = "a1"</code>, the output should be<br>
<code>alphanumericLess(s1, s2) = true</code>;</li>
<li>For <code>s1 = "ab"</code> and <code>s2 = "a1"</code>, the output should be<br>
<code>alphanumericLess(s1, s2) = false</code>;</li>
<li>For <code>s1 = "b"</code> and <code>s2 = "a1"</code>, the output should be<br>
<code>alphanumericLess(s1, s2) = false</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s1</strong></p>
<p>String, consisting of Latin letters and digits.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s1.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] string s2</strong></p>
<p>String, consisting of Latin letters and digits.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s2.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>s1</code> is alphanumerically strictly less than <code>s2</code>, <code>false</code> otherwise.</p>
</li>
</ul>
</div>