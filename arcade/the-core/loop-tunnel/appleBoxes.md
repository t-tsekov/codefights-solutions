<div class="markdown"><p>You have <code>k</code> apple boxes full of apples. Each square box of size <code>m</code> contains <code>m × m</code> apples. You just noticed two interesting properties about the boxes:</p>
<ol>
<li>The smallest box is size <code>1</code>, the next one is size <code>2</code>,..., all the way up to size <code>k</code>.</li>
<li>Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.</li>
</ol>
<p>Your task is to calculate the difference between the number of red apples and the number of yellow apples.</p>
<p><strong>Example</strong></p>
<p>For <code>k = 5</code>, the output should be<br>
<code>appleBoxes(k) = -15</code>.</p>
<p>There are <code>1 + 3 * 3 + 5 * 5 = 35</code> yellow apples and <code>2 * 2 + 4 * 4 = 20</code> red apples, making the answer <code>20 - 35 = -15</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer k</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 40</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The difference between the two types of apples.</p>
</li>
</ul>
</div>