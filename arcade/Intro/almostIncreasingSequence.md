<div class="markdown"><p>Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>sequence = [1, 3, 2, 1]</code>, the output should be<br>
<code>almostIncreasingSequence(sequence) = false</code>;</p>
<p>There is no one element in this array that can be removed in order to get a strictly increasing sequence.</p>
</li>
<li>
<p>For <code>sequence = [1, 3, 2]</code>, the output should be<br>
<code>almostIncreasingSequence(sequence) = true</code>.</p>
<p>You can remove <code>3</code> from the array to get the strictly increasing sequence <code>[1, 2]</code>. Alternately, you can remove <code>2</code> to get the strictly increasing sequence <code>[1, 3]</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer sequence</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ sequence.length ≤ 10<sup>5</sup></code>,<br>
<code>-10<sup>5</sup> ≤ sequence[i] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>