<div class="markdown"><p>The greatest ever Rock-Paper-Scissors Championship will take place in your town! The best <code>players</code> will battle each other to see who's the best player in the world. Each player will compete against each other player twice, once home and once away.</p>
<p>Given the list of the <code>players</code>, your task is to come up with the list of all the games between them, and return them sorted <a href="keyword://lexicographical-order-for-arrays">lexicographically</a>.</p>
<p><strong>Example</strong></p>
<p>For <code>players = ["trainee", "warrior", "ninja"]</code>, the output should be</p>
<pre><code>rockPaperScissors(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              ["trainee", "ninja"], ["trainee", "warrior"], 
                              ["warrior", "ninja"], ["warrior", "trainee"]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string players</strong></p>
<p>A list of distinct players, where each player is given by their nickname that can consist of English letters and whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ players.length ≤ 10</code>,<br>
<code>1 ≤ players[i].length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Array of pairs of players that will play against one another sorted <em>lexicographically</em>.</p>
<p><em>Note</em>: if your solution returns a list of tuples, the tuples will be converted to list automatically.</p>
</li>
</ul>
</div>