'<div class="markdown"><p>Each cell in a 2D grid contains either a wall (<code>'W'</code>) or an enemy (<code>'E'</code>), or is empty (<code>'0'</code>). Bombs can destroy enemies, but walls are too strong to be destroyed. A bomb placed in an empty cell destroys all enemies in the same row and column, but the destruction stops once it hits a wall.</p>
<p>Return the maximum number of enemies you can destroy using one bomb.</p>
<p><em>Note that your solution should have <code>O(field.length · field[0].length)</code> complexity because this is what you will be asked during an interview</em>.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>field = [["0", "0", "E", "0"],
         ["W", "0", "W", "E"],
         ["0", "E", "0", "W"],
         ["0", "W", "0", "E"]]
</code></pre>
<p>the output should be<br>
<code>bomber(field) = 2</code>.</p>
<p>Placing a bomb at <code>(0, 1)</code> or at <code>(0, 3)</code> destroys <code>2</code> enemies.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.char field</strong></p>
<p>A rectangular matrix containing characters <code>'0'</code>, <code>'W'</code> and <code>'E'</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ field.length ≤ 100</code>,<br>
<code>0 ≤ field[i].length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>'