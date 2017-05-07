<div class="markdown"><p>You are given two strings <code>s</code> and <code>t</code> of the same length, consisting of uppercase English letters. Your task is to find the minimum number of <em>"replacement operations"</em> needed to get some <a href="keyword://anagram">anagram</a> of the string <code>t</code> from the string <code>s</code>. A replacement operation is performed by picking exactly one character from the string <code>s</code> and replacing it by some other character.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>s = "AABAA"</code> and <code>t = "BBAAA"</code>, the output should be<br>
<code>createAnagram(s, t) = 1</code>;</li>
<li>For <code>s = "OVGHK"</code> and <code>t = "RPGUC"</code>, the output should be<br>
<code>createAnagram(s, t) = 4</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ s.length ≤ 35</code>.</p>
</li>
<li>
<p><strong>[input] string t</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>t.length = s.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum number of replacement operations needed to get an anagram of the string <code>t</code> from the string <code>s</code>.</p>
</li>
</ul>
</div>