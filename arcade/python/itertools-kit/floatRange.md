<div class="markdown"><p>As you may know, the <code>range</code> function in Python allows coders to iterate over elements from <code>start</code> to <code>stop</code> with the given <code>step</code>. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.</p>
<p>CodeFights doesn't include third-party libraries, so you have to make do with the standard ones. Given float numbers <code>start</code>, <code>stop</code> and <code>step</code>, your task is to return a list of values from <code>start</code> to <code>stop</code> (including <code>start</code> and not including <code>stop</code>), evenly spaced by the <code>step</code>.</p>
<p>Values <code>start</code>, <code>stop</code> and <code>step</code> have at most <code>5</code> digits after the decimal point each.</p>
<p><strong>Example</strong></p>
<p>For <code>start = -0.9</code>, <code>stop = 0.45</code> and <code>step = 0.2</code>,<br>
the output should be<br>
<code>floatRange(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] float start</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ start ≤ stop ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] float stop</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ start ≤ stop ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] float step</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 &lt; step ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.float</strong></p>
<p>A list of values in range <code>[start, stop)</code>, spaced by the <code>step</code>.</p>
</li>
</ul>
</div>