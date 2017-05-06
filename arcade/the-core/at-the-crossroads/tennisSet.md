<div class="markdown"><p>In tennis, a set is finished when one of the players wins <code>6</code> games and the other one wins less than <code>5</code>, or, if both players win at least <code>5</code> games, until one of the players win <code>7</code> games.</p>
<p>Determine if it is possible for a tennis set to be finished with the score <code>score1</code> : <code>score2</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>score1 = 3</code> and <code>score2 = 6</code>, the output should be<br>
<code>tennisSet(score1, score2) = true</code>;</li>
<li>For <code>score1 = 8</code> and <code>score2 = 5</code>, the output should be<br>
<code>tennisSet(score1, score2) = false</code>;</li>
<li>For <code>score1 = 6</code> and <code>score2 = 5</code>, the output should be<br>
<code>tennisSet(score1, score2) = false</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer score1</strong></p>
<p>Number of games won by the <code>1<sup>st</sup></code> player, non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ score1 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer score2</strong></p>
<p>Number of games won by the <code>2<sup>nd</sup></code> player, non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ score2 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>score1 : score2</code> represents a possible score for an ended set, <code>false</code> otherwise.</p>
</li>
</ul>
</div>