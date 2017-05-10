<div class="markdown"><p>You need to compress a large <code>document</code> that consists of a small number of different characters. To choose the best encoding algorithm, you would like to look closely at the characters that comprise this <code>document</code>.</p>
<p>Given a <code>document</code>, return an array of all unique characters that appear in it sorted by their ASCII codes.</p>
<p><strong>Example</strong></p>
<p>For <code>document = "Todd told Tom to trot to the timber"</code>,<br>
the output should be<br>
<code>uniqueCharacters(document) = [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't']</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string document</strong></p>
<p>A string consisting of English letters, whitespace characters and punctuation marks.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ document.length ≤ 80</code>.</p>
</li>
<li>
<p><strong>[output] array.char</strong></p>
<p>A sorted array of all the unique characters that appear in the <code>document</code>.</p>
</li>
</ul>
</div>