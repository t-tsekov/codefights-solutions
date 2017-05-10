<div class="markdown"><p>You're organizing murder mystery games for your coworkers, and came up with a lot of ideas for various groups of participants. The <code>i<sup>th</sup></code> 0-based game can be played only if there are at least <code>i</code> people registered for it. Game number <code>0</code> is a beta that you will try out with your friends, so there's no need for participants.</p>
<p>You're expecting a full house, since a lot of <code>participants</code> signed up already. Not too many, unfortunately: looks like some games can't be played, because too few people registered for them. Given the list of <code>participants</code>, your task is to return the list of games for which too few people signed up.</p>
<p><strong>Example</strong></p>
<p>For <code>participants = [0, 1, 1, 5, 4, 8]</code>, the output should be<br>
<code>checkParticipants(participants) = [2]</code>.</p>
<p>For the game number <code>2</code> (0-based) <code>2</code> people are required, but only one person has registered.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer participants</strong></p>
<p>The <code>i<sup>th</sup></code> element of the array contains the number of coworkers signed up for the <code>i<sup>th</sup></code> game.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ participants.length ≤ 100</code>,<br>
<code>0 ≤ participants[i] ≤ 150</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array of games for which too few people signed up.</p>
</li>
</ul>
</div>