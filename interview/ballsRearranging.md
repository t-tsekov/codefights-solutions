<div class="markdown"><p>An infinite number of boxes are arranged in a row and numbered from left to right. The first box on the left is number <code>1</code>, the next box is number <code>2</code>, etc. <code>n</code> balls are placed in <code>n</code> of the boxes, and there can only be one ball per box. You want to organize the balls, so you decide to arrange all the balls next to each other. They should occupy a contiguous set of boxes. You can take one ball and move it into an empty box in one move.</p>
<p>Given an array <code>balls</code> that indicates the numbers of the boxes in which the balls are placed, find the minimum number of moves needed to organize the balls.</p>
<p><strong>Example</strong></p>
<p>For <code>balls = [6, 4, 1, 7, 10]</code>, the output should be<br>
<code>ballsRearranging(balls) = 2</code>.</p>
<p>In this example, the minimum number of moves needed to arrange the balls next to each other is <code>2</code>. You could move the ball in box <code>1</code> to box <code>5</code> and the ball in box <code>10</code> to box <code>8</code> (or to box <code>3</code>).</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer balls</strong></p>
<p>An array of balls. The <code>i<sup>th</sup></code> element indicates the number of the box where the <code>i<sup>th</sup></code> ball is placed. It is guaranteed that all the elements in the array are distinct.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ balls.length ≤ 10<sup>5</sup></code>,<br>
<code>1 ≤ balls[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum number of moves needed to organize the balls into a contiguous set of boxes.</p>
</li>
</ul>
</div>