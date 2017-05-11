<div class="markdown"><p>Although Python does provide a bunch of useful built-in functions, some of them are simply missing for no apparent reason. One example of such function is a <code>sign</code> function implemented in many other languages. <code>sign(x)</code> returns <code>1</code> if <code>x</code> is positive, <code>-1</code> if <code>x</code> is negative, and <code>0</code> if <code>x</code> is equal to zero.</p>
<p>You decided to build your own package of useful functions, and would like to start with the <code>sign</code> function. Given the value of <code>x</code>, return the result of applying the <code>sign</code> function to it.</p>
<p><strong>Example</strong></p>
<p>For <code>x = -34</code>, the output should be<br>
<code>sign(x) = -1</code>.</p>
<p><code>-34</code> is a negative number, thus the output should be <code>-1</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer x</strong></p>
<p>The argument of the <code>sign</code> function.</p>
<p><em>Guaranteed constraints:</em><br>
<code>-50 ≤ x ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The value of <code>sign(x)</code>.</p>
</li>
</ul>
</div>