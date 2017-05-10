<div class="markdown"><p>Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of <code>numbers</code>, Billy should calculate the following value:</p>
<pre><code>(((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
</code></pre>
<p>Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of <code>numbers</code>, will return the result of the operation <code>Billy</code> has to perform.</p>
<p><strong>Example</strong></p>
<p>For <code>numbers = [1, 2, 3, 4, 5, 6]</code>, the output should be<br>
<code>mathPractice(numbers) = 71</code>.</p>
<p>Here's how the answer is obtained: <code>((1 + 2) * 3 + 4) * 5 + 6 = 71</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer numbers</strong></p>
<p>A list of numbers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ numbers.length ≤ 20</code>,<br>
<code>0 ≤ numbers[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The answer Billy should obtain.</p>
</li>
</ul>
</div>