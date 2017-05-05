<div class="markdown"><p>Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.</p>
<p><strong>Example</strong></p>
<p>For <code>a = [-1, 150, 190, 170, -1, -1, 160, 180]</code>, the output should be<br>
<code>sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>If <code>a[i] = -1</code>, then the <code>i<sup>th</sup></code> position is occupied by a tree. Otherwise <code>a[i]</code> is the height of a person standing in the <code>i<sup>th</sup></code> position.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ a.length ≤ 15</code>,<br>
<code>-1 ≤ a[i] ≤ 200</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Sorted array <code>a</code> with all the trees untouched.</p>
</li>
</ul>
</div>