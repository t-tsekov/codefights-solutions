<div class="markdown"><p>At CodeFights the CodeFighters can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.</p>
<p>Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of <code>codefighters</code>.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>codefighters = [["warrior", "1", "1050"],
                ["Ninja!",  "21", "995"],
                ["recruit", "3", "995"]]
</code></pre>
<p>the output should be<br>
<code>sortCodefighters(codefighters) = ["warrior", "recruit", "Ninja!"]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.string codefighters</strong></p>
<p>A list of CodeFighters, where each CodeFighter is given in the format <code>[<em>username</em>, <em>id</em>, <em>xp</em>]</code>.<br>
It is guaranteed that all usernames and ids are unique.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ codefighters.length ≤ 10<sup>4</sup></code>,<br>
<code>codefighters[i].length = 3</code>,<br>
<code>1 ≤ codefighters[i][0].length ≤ 20</code>,<br>
<code>1 ≤ int(codefighters[i][1]), int(codefighters[i][2]) ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A list of CodeFighters sorted as described above.</p>
</li>
</ul>
</div>