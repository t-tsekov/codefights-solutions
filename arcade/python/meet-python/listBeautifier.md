<div class="markdown"><p>Let's call a list <em>beautiful</em> if its first element is equal to its last element, or if a list is empty. Given a list <code>a</code>, your task is to chop off its first and its last element until it becomes <em>beautiful</em>. Implement a function that will make the given <code>a</code> <em>beautiful</em> as described, and return the resulting list as an answer.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>a = [3, 4, 2, 4, 38, 4, 5, 3, 2]</code>, the output should be<br>
<code>listBeautifier(a) = [4, 38, 4]</code>.</p>
<p>Here's how the answer is obtained:<br>
<code>[3, 4, 2, 4, 38, 4, 5, 3, 2]</code> =&gt; <code>[4, 2, 4, 38, 4, 5, 3]</code> =&gt; <code>[2, 4, 38, 4, 5]</code> =&gt; <code>[4, 38, 4]</code>.</p>
</li>
<li>
<p>For <code>a = [1, 4, -5]</code>, the output should be<br>
<code>listBeautifier(a) = [4]</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>A list of integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ a.length ≤ 50</code>,<br>
<code>1 ≤ a[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A <em>beautiful</em> list obtained as described above.</p>
</li>
</ul>
</div>