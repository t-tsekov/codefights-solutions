<div class="markdown"><p>Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.</p>
<p>The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.</p>
<p>Given the total number of rows and columns in the theater (<code>nRows</code> and <code>nCols</code>, respectively), and the <code>row</code> and <code>column</code> you're sitting in, return the number of people who sit strictly behind you <strong>and</strong> in your column or to the left, assuming all seats are occupied.</p>
<p><strong>Example</strong></p>
<p>For <code>nCols = 16</code>, <code>nRows = 11</code>, <code>col = 5</code> and <code>row = 3</code>, the output should be<br>
<code>seatsInTheater(nCols, nRows, col, row) = 96</code>.</p>
<p>Here is what the theater looks like:<br>
<img src="https://codefightsuserpics.s3.amazonaws.com/tasks/seatsInTheater/img/example.png?_tm=1491302298590" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer nCols</strong></p>
<p>An integer, the number of theater's columns.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ nCols ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer nRows</strong></p>
<p>An integer, the number of theater's rows.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ nRows ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer col</strong></p>
<p>An integer, the column number of your own seat (1-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ col ≤ nCols</code>.</p>
</li>
<li>
<p><strong>[input] integer row</strong></p>
<p>An integer, the row number of your own seat (1-based).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ row ≤ nRows</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of people who sit strictly behind you <strong>and</strong> in your column or to the left.</p>
</li>
</ul>
</div>