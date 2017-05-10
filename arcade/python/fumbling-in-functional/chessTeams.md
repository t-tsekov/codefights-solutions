<div class="markdown"><p>A grand Team Chess Tournament will be held at your University. Two teams, <code>smarties</code> and <code>cleveries</code>, will clash to determine whose chess skills are better. The teams have the same number of members, and the <code>i<sup>th</sup></code> member of <code>smarties</code> will play against the <code>i<sup>th</sup></code> member of <code>cleveries</code> in the <code>i<sup>th</sup></code> game for each valid <code>i</code></p>
<p>Given the names of the players of both <code>smarties</code> and <code>cleveries</code>, return the games in the order they will be played.</p>
<p><strong>Example</strong></p>
<p>For <code>smarties = ["Jane", "Bob", "Peter"]</code> and<br>
<code>cleveries = ["Oscar", "Lidia", "Ann"]</code>, the output should be</p>
<pre><code>chessTeams(smarties, cleveries) = [["Jane",  "Oscar"],
                                   ["Bob",   "Lidia"],
                                   ["Peter", "Ann"]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string smarties</strong></p>
<p>Array of strings, where each string is the name of the member of <code>smarties</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ smarties.length ≤ 10</code>,<br>
<code>2 ≤ smarties[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.string cleveries</strong></p>
<p>Members of <code>cleveries</code> in the same format as <code>smarties</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>cleveries.length = smarties.length</code>,<br>
<code>2 ≤ cleveries[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>The games in the following format: <code>[game<sub>0</sub>, game<sub>1</sub>, ..., game<sub>smarties.length - 1</sub>]</code> where <code>game<sub>i</sub> = [smarty<sub>i</sub>, clevery<sub>i</sub>]</code>.</p>
</li>
</ul>
</div>