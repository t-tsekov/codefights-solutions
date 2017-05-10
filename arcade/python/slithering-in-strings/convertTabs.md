<div class="markdown"><p>You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.</p>
<p>Implement a function that, given a piece of <code>code</code> and a positive integer <code>x</code> will turn each tabulation character in <code>code</code> into <code>x</code> whitespace characters.</p>
<p><strong>Example</strong></p>
<p>For <code>code = "\treturn False"</code> and <code>x = 4</code>, the output should be<br>
<code>convertTabs(code, x) = "&nbsp;&nbsp;&nbsp;&nbsp;return False"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string code</strong></p>
<p>Your piece of code.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ code.length ≤ 1500</code>.</p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>The number of whitespace characters (<code>' '</code>) that should replace each occurrence of the tabulation character (<code>'\t'</code>).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ x ≤ 16</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The given <code>code</code> with tabulation characters expanded according to <code>x</code>.</p>
</li>
</ul>
</div>