<div class="markdown"><p>Imagine a white rectangular grid of <code>n</code> rows and <code>m</code> columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:</p>
<ul>
<li>A cell is painted black if it has at least one point in common with the diagonal;</li>
<li>Otherwise, a cell is painted white.</li>
</ul>
<p>Count the number of cells painted black.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 3</code> and <code>m = 4</code>, the output should be<br>
<code>countBlackCells(n, m) = 6</code>.</p>
<p>There are <code>6</code> cells that have at least one common point with the diagonal and therefore are painted black.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/countBlackCells/img/example1.jpg?_tm=1490625755747" alt=""></p>
</li>
<li>
<p>For <code>n = 3</code> and <code>m = 3</code>, the output should be<br>
<code>countBlackCells(n, m) = 7</code>.</p>
<p><code>7</code> cells have at least one common point with the diagonal and are painted black.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/countBlackCells/img/example2.jpg?_tm=1490625755909" alt=""></p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of rows.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer m</strong></p>
<p>The number of columns.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ m ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of black cells.</p>
</li>
</ul>
</div>