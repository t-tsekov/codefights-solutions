<div class="markdown"><p>Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).</p>
<p>If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.</p>
<p>For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If there will be no meetings, return <code>-1</code> instead.</p>
<p><strong>Example</strong></p>
<p>For <code>startPosition = [1, 4, 2]</code> and <code>speed = [27, 18, 24]</code>, the output should be<br>
<code>runnersMeetings(startPosition, speed) = 3</code>.</p>
<p>In 20 seconds after the runners start running, they end up at the same point. Check out the gif below for better understanding:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/runnersMeetings/img/example.gif?_tm=1491302292681" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer startPosition</strong></p>
<p>A non-empty array of integers representing starting positions of runners (in meters).</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ startPosition.length ≤ 10</code>,<br>
<code>-1000 ≤ startPosition[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.integer speed</strong></p>
<p>Array of positive integers of the same length as <code>startPosition</code> representing speeds of the runners (in meters per minute).</p>
<p><em>Guaranteed constraints:</em><br>
<code>speed.length = startPosition.length</code>,<br>
<code>1 ≤ speed[i] ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The maximum meeting cardinality or <code>-1</code> if there will be no meetings.</p>
</li>
</ul>
</div>