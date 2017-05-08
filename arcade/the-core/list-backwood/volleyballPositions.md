<div class="markdown"><p>You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.</p>
<p>The team you favor plays in the following formation:</p>
<pre><code>0 3 0
4 0 2
0 6 0
5 0 1
</code></pre>
<p>where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position <code>2</code> moves to position <code>1</code>, the player in position <code>3</code> moves to position <code>2</code>, and so on, with the player in position <code>1</code> moving to position <code>6</code>.</p>
<p>Here's how the players change their positions:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/volleyballPositions/img/example.png?_tm=1491409891893" alt=""></p>
<p>Given the current <code>formation</code> of the team and the number of times <code>k</code> it gained the serve, find the initial position of each player in it.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>formation = [["empty",   "Player5", "empty"],
             ["Player4", "empty",   "Player2"],
             ["empty",   "Player3", "empty"],
             ["Player6", "empty",   "Player1"]]
</code></pre>
<p>and <code>k = 2</code>, the output should be</p>
<pre><code>volleyballPositions(formation, k) = [
    ["empty",   "Player1", "empty"],
    ["Player2", "empty",   "Player3"],
    ["empty",   "Player4", "empty"],
    ["Player5", "empty",   "Player6"]
]
</code></pre>
</li>
<li>
<p>For</p>
<pre><code>formation = [["empty", "Alice", "empty"],
             ["Bob",   "empty", "Charlie"],
             ["empty", "Dave",  "empty"],
             ["Eve",   "empty", "Frank"]]
</code></pre>
<p>and <code>k = 6</code>, the output should be</p>
<pre><code>volleyballPositions(formation, k) = [
    ["empty", "Alice", "empty"],
    ["Bob",   "empty", "Charlie"],
    ["empty", "Dave",  "empty"],
    ["Eve",   "empty", "Frank"]
]
</code></pre>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.string formation</strong></p>
<p>A <code>4 × 3</code> array of strings representing names of the players in the positions corresponding to those in the schema above.<br>
It is guaranteed that for each empty position the corresponding element of <code>formation</code> is <code>"empty"</code>.<br>
It is also guaranteed that there is no player called <code>"empty"</code> in the team.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number of times the team gained the serve.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ k ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Team arrangement at the start of the game.</p>
</li>
</ul>
</div>