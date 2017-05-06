<div class="markdown"><p>Given integers <code>a</code> and <code>b</code>, determine whether the following pseudocode results in an infinite loop</p>
<pre><code>while a is not equal to b do
  increase a by 1
  decrease b by 1
</code></pre>
<p>Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>a = 2</code> and <code>b = 6</code>, the output should be<br>
<code>isInfiniteProcess(a, b) = false</code>;</li>
<li>For <code>a = 2</code> and <code>b = 3</code>, the output should be<br>
<code>isInfiniteProcess(a, b) = true</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ a ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ b ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the pseudocode will never stop, <code>false</code> otherwise.</p>
</li>
</ul>
</div>