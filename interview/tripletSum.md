<div class="markdown"><p><em>Note: Write a solution with <code>O(n<sup>2</sup>)</code> time complexity, since this is what you would be asked to do during a real interview.</em></p>
<p>You have an array <code>a</code> composed of exactly <code>n</code> elements. Given a number <code>x</code>, determine whether or not <code>a</code> contains three elements for which the sum is exactly <code>x</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>x = 15</code> and <code>a = [14, 1, 2, 3, 8, 15, 3]</code>, the output should be<br>
<code>tripletSum(x, a) = false</code>;</p>
</li>
<li>
<p>For <code>x = 8</code> and <code>a = [1, 1, 2, 5, 3]</code>, the output should be<br>
<code>tripletSum(x, a) = true</code>.</p>
<p>The given array contains the elements <code>1</code>,<code>2</code>, and <code>5</code>, which add up to <code>8</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer x</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ x ≤ 3000</code>.</p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ a.length ≤ 1000</code>,<br><br>
<code>1 ≤ a[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if the array contains three elements that add up to <code>x</code> and <code>false</code> otherwise.</p>
</li>
</ul>
</div>