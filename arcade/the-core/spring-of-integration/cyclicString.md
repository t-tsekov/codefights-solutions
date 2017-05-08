<div class="markdown"><p>You're given a <a href="keyword://substring">substring</a> <code>s</code> of some <a href="keyword://cyclic-string">cyclic string</a>. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?</p>
<p><strong>Example</strong></p>
<p>For <code>s = "cabca"</code>, the output should be<br>
<code>cyclicString(s) = 3</code>.</p>
<p><code>"cabca"</code> is a substring of a cycle string <code>"abcabcabcabc..."</code> that can be obtained by concatenating <code>"abc"</code> to itself. Thus, the answer is <code>3</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ s.length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>