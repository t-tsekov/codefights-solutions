<div class="markdown"><p>A noob programmer was given two simple tasks: sum and sort the elements of the given array<br>
<code>a = [a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>]</code>. He started with summing and did it easily, but decided to store the sum he found in some random position of the original array which was a bad idea. Now he needs to cope with the second task, sorting the original array <code>a</code>, and it's giving him trouble since he modified it.</p>
<p>Given the array <code>shuffled</code>, consisting of elements <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, a<sub>1</sub> + a<sub>2</sub> + ... + a<sub>n</sub></code> in random order, return the sorted array of original elements <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>shuffled = [1, 12, 3, 6, 2]</code>, the output should be<br>
<code>shuffledArray(shuffled) = [1, 2, 3, 6]</code>.</p>
<p><code>1 + 3 + 6 + 2 = 12</code>, which means that <code>1</code>, <code>3</code>, <code>6</code> and <code>2</code> are original elements of the array.</p>
</li>
<li>
<p>For <code>shuffled = [1, -3, -5, 7, 2]</code>, the output should be<br>
<code>shuffledArray(shuffled) = [-5, -3, 2, 7]</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer shuffled</strong></p>
<p>Array of at least two integers. It is guaranteed that there is an index <code>i</code> such that <code>shuffled[i] = shuffled[0] + ... + shuffled[i - 1] + shuffled[i + 1] + ... + shuffled[n]</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ shuffled.length ≤ 15</code>,<br>
<code>-300 ≤ shuffled[i] ≤ 300</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array of <code>shuffled.length - 1</code> elements.</p>
</li>
</ul>
</div>