<div class="markdown"><p>When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a <code>note</code> with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit <code>0</code> is replaced with <code>'a'</code>, <code>1</code> is replaced with <code>'b'</code> and so on, with digit <code>9</code> replaced by <code>'j'</code>.</p>
<p>The <code>note</code> is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.</p>
<p><strong>Example</strong></p>
<p>For <code>note = "you'll n4v4r 6u4ss 8t: cdja"</code>, the output should be<br>
<code>stolenLunch(note) = "you'll never guess it: 2390"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string note</strong></p>
<p>A string consisting of lowercase English letters, digits, punctuation marks and whitespace characters (<code>' '</code>).</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ note.length ≤ 500</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The deciphered <code>note</code>.</p>
</li>
</ul>
</div>