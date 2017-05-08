<div class="markdown"><p>You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
</code></pre>
<p>the output should be <code>gravitation(rows) = [1, 4]</code>.</p>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/gravitation/img/example.png?_tm=1490626014449" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string rows</strong></p>
<p>A non-empty array of strings of equal length consisting only of <code>#</code>-s and <code>.</code>-s describing the box at a specific moment in time. Sharps represent stones, and dots represent empty cells. <code>row[0]</code> corresponds to the upper row. Last element of <code>rows</code> corresponds to the ground level.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ rows.length ≤ 10</code>,<br>
<code>2 ≤ rows[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array containing numbers of all columns (leftmost column's number is <code>0</code>) in which movements will stop at the same second and earlier than in any other column. Assume that if there are no stones in a column then movement stops immediately, i.e. after <code>0</code> seconds.</p>
</li>
</ul>
</div>