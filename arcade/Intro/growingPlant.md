<div class="markdown"><p>Each day a plant is growing by <code>upSpeed</code> meters. Each night that plant's height decreases by <code>downSpeed</code> meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.</p>
<p><strong>Example</strong></p>
<p>For <code>upSpeed = 100</code>, <code>downSpeed = 10</code> and <code>desiredHeight = 910</code>, the output should be<br>
<code>growingPlant(upSpeed, downSpeed, desiredHeight) = 10</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer upSpeed</strong></p>
<p>A positive integer representing the daily growth.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ upSpeed ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] integer downSpeed</strong></p>
<p>A positive integer representing the nightly decline.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ downSpeed &lt; upSpeed</code>.</p>
</li>
<li>
<p><strong>[input] integer desiredHeight</strong></p>
<p>A positive integer representing the threshold.</p>
<p><em>Guaranteed constraints:</em><br>
<code>4 ≤ desiredHeight ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of days that it will take for the plant to reach/pass <code>desiredHeight</code> (including the last day in the total count).</p>
</li>
</ul>
</div>