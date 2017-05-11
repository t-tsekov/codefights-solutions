<div class="markdown"><p>An you may know, the <code>range</code> function in Python allows coders to iterate over elements from <code>start</code> to <code>stop</code> with the given <code>step</code>. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.</p>
<p>CodeFights doesn't include third-party libraries, so you have to make do with the standard ones. Given array of arguments <code>args</code>, return array of values the float range generator should return.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>args = [5]</code>, the output should be<br>
<code>rangeFloat(args) = [0, 1, 2, 3, 4]</code>.</p>
<p>Since <code>args</code> contains only one element, it corresponds to the <code>stop</code> argument. <code>start</code> and <code>step</code> arguments have default parameters, which are <code>0</code> and <code>1</code>, respectively.</p>
</li>
<li>
<p>For <code>args = [0.5, 7.5]</code>, the output should be<br>
<code>rangeFloat(args) = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]</code>.</p>
<p>There are only two elements in <code>args</code>, which means that the first value corresponds to <code>start</code>, and the second value corresponds to <code>stop</code>. The <code>step</code> argument thus has a default value, which is <code>1</code>.</p>
</li>
<li>
<p>For <code>args = [-1.1, 2.4, 0.3]</code>, the output should be<br>
<code>rangeFloat(args) = [-1.1, -0.8, -0.5, -0.2, 0.1, 0.4, 0.7, 1, 1.3, 1.6, 1.9, 2.2]</code>.</p>
<p>Since <code>args</code> contains all three elements, the values of <code>start</code>, <code>stop</code> and <code>step</code> are <code>-1.1</code>, <code>2.4</code> and <code>0.3</code>, respectively.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.float args</strong></p>
<p>A list of arguments.</p>
<ul>
<li>If <code>args</code> consists of one element, the result should be <code>range(args[0])</code>.</li>
<li>If <code>args</code> consists of two elements, the result should be <code>range(args[0], args[1])</code>.</li>
<li>If <code>args</code> consists of three elements, the result should be <code>range(args[0], args[1], args[2])</code>.</li>
</ul>
<p>Note, that the function should also work with negative values of <code>step</code>. For more information on how the built-in <code>range</code> function works, check out <a href="https://docs.python.org/2/library/functions.html#range">this</a> page.</p>
<p>If is guaranteed, that if <code>args.length == 3</code>, then <code>args[2] ≠ 0</code>.</p>
<p>All values are given with at most <code>3</code> digits after the decimal point.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ args.length ≤ 3</code>,<br>
<code>-1000 ≤ args[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.float</strong></p>
<p>A list which python built-in <code>range</code> would produce if it supported float values.</p>
</li>
</ul>
</div>