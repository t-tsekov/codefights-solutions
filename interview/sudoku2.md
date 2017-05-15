<div class="markdown"><p><em>Sudoku</em> is a number-placement puzzle. The objective is to fill a <code>9 × 9</code> grid with numbers in such a way that each column, each row, and each of the nine <code>3 × 3</code> sub-grids that compose the grid <em>all</em> contain <em>all</em> of the numbers from <code>1</code> to <code>9</code> one time.</p>
<p>Implement an algorithm that will check whether the given <code>grid</code> of numbers represents a valid <em>Sudoku</em> puzzle according to the layout rules described above. Note that the puzzle represented by <code>grid</code> does not have to be solvable.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
</code></pre>
<p>the output should be<br>
<code>sudoku2(grid) = true</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
</code></pre>
<p>the output should be<br>
<code>sudoku2(grid) = false</code>.</p>
<p>The given <code>grid</code> is not correct because there are two <code>1</code>s in the second column. Each column, each row, and each <code>3 × 3</code> subgrid can only contain the numbers <code>1</code> through <code>9</code> one time.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.char grid</strong></p>
<p>A <code>9 × 9</code> array of characters, in which each character is either a digit from <code>'1'</code> to <code>'9'</code> or a period <code>'.'</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if <code>grid</code> represents a valid <em>Sudoku</em> puzzle, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>