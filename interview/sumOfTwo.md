<div class="markdown"><p>You have two integer arrays, <code>a</code> and <code>b</code>, and an integer target value <code>v</code>. Determine whether there is a pair of numbers, where one number is taken from <code>a</code> and the other from <code>b</code>, that can be added together to get a sum of <code>v</code>. Return <code>true</code> if such a pair exists, otherwise return <code>false</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [1, 2, 3]</code>, <code>b = [10, 20, 30, 40]</code>, and <code>v = 42</code>, the output should be<br>
<code>sumOfTwo(a, b, v) = true</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>An array of integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ a.length ≤ 10<sup>5</sup></code>,<br>
<code>-10<sup>9</sup> ≤ a[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.integer b</strong></p>
<p>An array of integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ b.length ≤ 10<sup>5</sup></code>,<br>
<code>-10<sup>9</sup> ≤ b[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer v</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>-10<sup>9</sup> ≤ v ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if there are two elements from <code>a</code> and <code>b</code> which add up to <code>v</code>, and <code>false</code> otherwise.</p>
</li>
</ul>
</div>