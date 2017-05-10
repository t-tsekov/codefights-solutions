<div class="markdown"><p>You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a <em>power</em> value to each action and each word. To begin somewhere, you defined a <em>power</em> of a <code>word</code> as the sum of <em>powers</em> of its characters, where <em>power</em> of a character is equal to its 1-based index in the <a href="keyword://plaintext-alphabet">plaintext alphabet</a>.</p>
<p>Given a <code>word</code>, calculate its <em>power</em>.</p>
<p><strong>Example</strong></p>
<p>For <code>word = "hello"</code>, the output should be<br>
<code>wordPower(word) = 52</code>.</p>
<p>Letters <code>'h'</code>, <code>'e'</code>, <code>'l'</code> and <code>'o'</code> have <em>powers</em> <code>8</code>, <code>5</code>, <code>12</code> and <code>15</code>, respectively. Thus, the total power of the <code>word</code> is <code>8 + 5 + 12 + 12 + 15 = 52</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string word</strong></p>
<p>A string consisting of lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ word.length ≤ 25</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p><em>Power</em> of the given <code>word</code>.</p>
</li>
</ul>
</div>