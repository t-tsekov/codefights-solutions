<div class="markdown"><p>You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.</p>
<p>Given the starting HTML tag, find the appropriate end tag which your editor should propose.</p>
<p>If you are not familiar with HTML, consult with <a href="keyword://html-rules-for-tags">this note</a>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>startTag = "&lt;button type='button' disabled&gt;"</code>, the output should be<br>
<code>htmlEndTagByStartTag(startTag) = "&lt;/button&gt;"</code>;</li>
<li>For <code>startTag = "&lt;i&gt;"</code>, the output should be<br>
<code>htmlEndTagByStartTag(startTag) = "&lt;/i&gt;"</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string startTag</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ startTag.length ≤ 75</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
</div>