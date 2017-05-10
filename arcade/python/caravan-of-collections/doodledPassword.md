<div class="markdown"><p>Your friend has been doodling during the lecture and wrote down several digits in a circle. You're wondering if these <code>digits</code> might form the password to your friend's computer. You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the <code>digits</code> written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.</p>
<p>Given a list of <code>digits</code> as they are written in the clockwise order, find all other combinations the password could possibly have.</p>
<p><strong>Example</strong></p>
<p>For <code>digits = [1, 2, 3, 4, 5]</code>, the output should be</p>
<pre><code>doodledPassword(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                           [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
</code></pre>
<p>Here's what your friend wrote down:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/doodledPassword/img/example.png?_tm=1490625885530" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer digits</strong></p>
<p>The list of digits your friend wrote down.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ digits.length ≤ 20</code>,<br>
<code>0 ≤ digits[i] ≤ 9</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>All possible password combinations in the following order: first the combination starting with <code>digits[0]</code> should go, then the one starting with <code>digits[1]</code>, etc. The last combination should start with <code>digits[digits.length - 1]</code></p>
</li>
</ul>
</div>