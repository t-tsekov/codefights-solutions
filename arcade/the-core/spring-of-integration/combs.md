<div class="markdown"><p>Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.</p>
<p>It is guaranteed that there is at least one tooth at each end of the comb.<br>
It is also guaranteed that the total length of two strings is smaller than <code>32</code>.<br>
Note, that the combs can <strong>not</strong> be rotated/reversed.</p>
<p><strong>Example</strong></p>
<p>For <code>comb1 = "*..*"</code> and <code>comb2 = "*.*"</code>, the output should be<br>
<code>combs(comb1, comb2) = 5</code>.</p>
<p>Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/combs/img/cbs.png?_tm=1490625710921" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string comb1</strong></p>
<p>A comb is represented as a string. If there is an asterisk (<code>'*'</code>) in the <code>i<sup>th</sup></code> position, there is a tooth there. Otherwise there is a dot (<code>'.'</code>), which means there is a missing tooth on the comb.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ comb1.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string comb2</strong></p>
<p>The second comb is represented in the same way as the first one.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ comb2.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum length of a purse Miss X needs.</p>
</li>
</ul>
</div>