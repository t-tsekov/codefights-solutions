<div class="markdown"><p>Looks like your little brother doesn't want to remember the multiplication table! Instead he wants to play videogames all day long. To teach him a lesson you'd like to write a virus that will pop up in the middle of the game and disappear only when the brother correctly solves several math questions.</p>
<p>To begin with, you need to construct a multiplication table. Given an integer <code>n</code>, return the multiplication table of size <code>n × n</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 5</code>, the output should be</p>
<pre><code>multiplicationTable(n) = [[1, 2,  3,  4,  5 ], 
                          [2, 4,  6,  8,  10], 
                          [3, 6,  9,  12, 15], 
                          [4, 8,  12, 16, 20], 
                          [5, 10, 15, 20, 25]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>The size of the multiplication table.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ n ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>Multiplication table of size <code>n × n</code>, i.e. a square matrix that has value <code>i * j</code> at the intersection of the <code>i<sup>th</sup></code> row and the <code>j<sup>th</sup></code> column (both 1-based).</p>
</li>
</ul>
</div>