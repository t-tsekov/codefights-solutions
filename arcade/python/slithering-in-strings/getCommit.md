<div class="markdown"><p>The Abanamama Version System (AVS) is a software versioning and revision control system used in highly secure environments. In this system, each commit is assigned a unique name, the first part of which consists of the username encrypted in the base-4 system using symbols <code>'0'</code>, <code>'?'</code>, <code>'+'</code>, and <code>'!'</code>, and the second part consists of symbols of English alphabet.</p>
<p>Given such <code>commit</code>, your task is go remove the username part from it and return the second part as an answer.</p>
<p><strong>Example</strong></p>
<p>For <code>commit = "0??+0+!!someCommIdhsSt"</code>, the output should be<br>
<code>getCommit(commit) = "someCommIdhsSt"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string commit</strong></p>
<p>Commit in the format given above. Note, that it is possible that it doesn't contain the first or the second part.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ commit.length ≤ 45</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The second part of the <code>commit</code>.</p>
</li>
</ul>
</div>