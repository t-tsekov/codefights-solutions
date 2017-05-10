<div class="markdown"><p>For the opening ceremony of the upcoming sports event an even number of athletes were picked. They formed a <em>correct</em> lineup, i.e. such a lineup in which no two boys or two girls stand together. The first person in the lineup was a girl. As a part of the performance, adjacent pairs of athletes (i.e. the first one together with the second one, the third one together with the fourth one, etc.) had to swap positions with each other.</p>
<p>Given a list of <code>athletes</code>, return the list of <code>athletes</code> after the changes, i.e. after each adjacent pair of athletes is swapped.</p>
<p><strong>Example</strong></p>
<p>For <code>athletes = [1, 2, 3, 4, 5, 6]</code>, the output should be<br>
<code>correctLineup(athletes) = [2, 1, 4, 3, 6, 5]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer athletes</strong></p>
<p>A list of even length representing the athletes, where each athlete is given by the number written on their back.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ athletes.length ≤ 20</code>,<br>
<code>1 ≤ athletes[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array of <code>athletes</code> with each pair of adjacent elements swapped.</p>
</li>
</ul>
</div>