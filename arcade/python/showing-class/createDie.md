<div class="markdown"><p>Don Corletwo, local Mafia boss, asked you for a favor, and you, naturally, cannot say no. An yahtzee championship will be held soon enough, and Don needs to make sure that his player has a decent chance to win. You are assigned with the task of writing the dice interface for the game. As a Python programmer, you can use the <code>random</code> module to generate random numbers that will determine the result of throwing an <code>n</code>-sides die.</p>
<p>Of course, <code>random</code> module can get predictable results if given a proper <code>seed</code> value. Your task is to implement a function that, given the <code>seed</code> for <code>random</code> module and the number of sides on the die <code>n</code>, will return the value on the die using the following formula: <code>int(random.random() * n) + 1</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>seed = 37237</code> and <code>n = 5</code>, the output should be<br>
<code>createDie(seed, n) = 3</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer seed</strong></p>
<p>The seed for <code>random</code> module.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ seed ≤ 50000</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of sides on a die.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ n ≤ 12</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number obtained by rolling the die generated as described above.</p>
</li>
</ul>
</div>