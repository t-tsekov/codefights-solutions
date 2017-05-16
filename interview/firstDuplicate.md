<div class="markdown"><p><em>Note: Write a solution with <code>O(n)</code> time complexity and <code>O(1)</code> additional space complexity, since this is what you would be asked to do during a real interview.</em></p>
<p>Given an array <code>a</code> that contains only numbers in the range from <code>1</code> to <code>a.length</code>, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return <code>-1</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>a = [2, 3, 3, 1, 5, 2]</code>, the output should be<br>
<code>firstDuplicate(a) = 3</code>.</p>
<p>There are <code>2</code> duplicates: numbers <code>2</code> and <code>3</code>. The second occurrence of <code>3</code> has a smaller index than than second occurrence of <code>2</code> does, so the answer is <code>3</code>.</p>
</li>
<li>
<p>For <code>a = [2, 4, 3, 5, 1]</code>, the output should be<br>
<code>firstDuplicate(a) = -1</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ a.length ≤ 10<sup>5</sup></code>,<br>
<code>1 ≤ a[i] ≤ a.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The element in <code>a</code> that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return <code>-1</code>.</p>
</li>
</ul>
</div>