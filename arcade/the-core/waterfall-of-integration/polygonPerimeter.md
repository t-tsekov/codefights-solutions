<div class="markdown"><p>You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.</p>
<p>Find the perimeter of the black figure assuming that a single cell has unit length.</p>
<p>It's guaranteed that there is at least one black cell on the table.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
</code></pre>
<p>the output should be<br>
<code>polygonPerimeter(matrix) = 12</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/polygonPerimeter/img/example1.png?_tm=1490636490133" alt=""></p>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
</code></pre>
<p>the output should be<br>
<code>polygonPerimeter(matrix) = 16</code>.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/polygonPerimeter/img/example2.png?_tm=1490636490343" alt=""></p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.boolean matrix</strong></p>
<p>A matrix of booleans representing the rectangular board where <code>true</code> means a <em>black</em> cell and <code>false</code> means a <em>white</em> one.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ matrix.length ≤ 5</code>,<br>
<code>2 ≤ matrix[0].length ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>