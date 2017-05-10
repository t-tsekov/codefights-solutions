def createHistogram(ch, data):
<div class="markdown"><p>You noticed that one of your employees has a weird performance rate: although his performance is usually good and stable, from time to time it drops drastically. You suspect it has something to do with the famous Code of Clones series: new episodes started to come out recently, and everyone watches and rewatches them every so often.</p>
<p>To confirm your theory, you'd like to create a histogram showing the number of assignments he completed each day in the given period. Given this <code>data</code>, return a list representing a horizontal histogram, where each bar is formed by the given character <code>ch</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>ch = '*'</code> and <code>data = [12, 12, 14, 3, 12, 15, 14]</code>,<br>
the output should be</p>
<pre><code>createHistogram(ch, data) = ["************",
                             "************",
                             "**************",
                             "***",
                             "************",
                             "***************",
                             "**************"]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] char ch</strong></p>
<p>A character that should compose the histogram.</p>
</li>
<li>
<p><strong>[input] array.integer data</strong></p>
<p>A list of assignments your employee completed each day during some period.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ data.length ≤ 20</code>,<br>
<code>0 ≤ data[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A histogram built as described above.</p>
</li>
</ul>
</div>