<div class="markdown"><p>You've been training your whole life, and now your dreams finally came true: you are a member of the best Crazyball team in the world! Unfortunately since your team is one of only two teams that play Crazyball, there are already many <code>players</code> in it, including yourself. For the starting lineup on the upcoming game the coach will pick <code>k</code> players, and you're curious if it's possible for you to make it there.</p>
<p>To calculate the odds of being a starter, you'd like to come up with a list of all possible lineups. Given the list of the <code>players</code> and the number of players <code>k</code> the coach has to pick, return all possible lineups sorted <a href="keyword://lexicographical-order-for-arrays">lexicographically</a>. Players in each lineup should also be sorted <a href="keyword://lexicographical-order-for-strings">lexicographically</a>.</p>
<p><strong>Example</strong></p>
<p>For <code>players = ["Ninja", "Warrior", "Trainee", "Newbie"]</code> and <code>k = 3</code>,<br>
the output should be</p>
<pre><code>crazyball(players, k) = [["Newbie", "Ninja", "Trainee"], 
                         ["Newbie", "Ninja", "Warrior"], 
                         ["Newbie", "Trainee", "Warrior"], 
                         ["Ninja", "Trainee", "Warrior"]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string players</strong></p>
<p>Array of distinct strings, where each string is player name. Each name may consist of English letters and whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ players.length ≤ 10</code>,<br>
<code>2 ≤ players[i].length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number of players the coach should pick for the lineup.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ players.length</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Array of all possible lineups sorted as described above.</p>
</li>
</ul>
</div>