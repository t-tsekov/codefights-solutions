<div class="markdown"><p>You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.</p>
<p>To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given <code>line</code> of your code with single ones. In addition, all leading and trailing whitespaces should be removed.</p>
<p><strong>Example</strong></p>
<p>For <code>line = "def&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;&nbsp;&nbsp;e&nbsp;&nbsp;gaDifficu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ltFun&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ction(x):"</code>,<br>
the output should be<br>
<code>catWalk(line) = "def m e gaDifficu ltFun ction(x):"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string line</strong></p>
<p>One line from your code containing way too many whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ line.length ≤ 125</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p><code>line</code> with unnecessary whitespace characters removed.</p>
</li>
</ul>
</div>