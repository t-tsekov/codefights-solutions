<div class="markdown"><p>A sentence is considered <em>correct</em> if:</p>
<ul>
<li>it starts with a capital letter;</li>
<li>it ends with a full stop, question mark or exclamation point (<code>'.'</code>, <code>'?'</code> or <code>'!'</code>);</li>
<li>full stops, question marks and exclamation points don't appear anywhere else in the sentence.</li>
</ul>
<p>Given a <code>sentence</code>, return <code>true</code> if it is correct and <code>false</code> otherwise.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>sentence = "This is an example of *correct* sentence."</code>,<br>
the output should be<br>
<code>isSentenceCorrect(sentence) = true</code>;</p>
</li>
<li>
<p>For <code>sentence = "!this sentence is TOTALLY incorrecT"</code>,<br>
the output should be<br>
<code>isSentenceCorrect(sentence) = false</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string sentence</strong></p>
<p>A string without newline characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ sentence.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given <code>sentence</code> is correct, <code>false</code> otherwise.</p>
</li>
</ul>
</div>