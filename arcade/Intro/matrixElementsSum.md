<div class="markdown"><p>After becoming famous, CodeBots decided to move to a new building and live together. The building is represented by a rectangular <code>matrix</code> of rooms, each cell containing an integer - the price of the room. Some rooms are <em>free</em> (their cost is <code>0</code>), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is <em>free</em> or is located anywhere below a <em>free</em> room in the same column is not considered suitable for the bots.</p>
<p>Help the bots calculate the total price of all the rooms that are suitable for them.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
</code></pre>
<p>the output should be<br>
<code>matrixElementsSum(matrix) = 9</code>.</p>
<p>Here's the rooms matrix with unsuitable rooms marked with <code>'x'</code>:</p>
<pre><code>[[x, 1, 1, 2], 
 [x, 5, x, x], 
 [x, x, x, x]]
</code></pre>
<p>Thus, the answer is <code>1 + 5 + 1 + 2 = 9</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>2-dimensional array of integers representing a rectangular matrix of the building.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ matrix.length ≤ 5</code>,<br>
<code>1 ≤ matrix[i].length ≤ 5</code>,<br>
<code>0 ≤ matrix[i][j] ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>