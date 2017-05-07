<div class="markdown"><p>You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.</p>
<p>The coin values available in Bananaland are stored in a sorted array <code>coins</code>. <code>coins[0] = 1</code>, and for each <code>i (0 &lt; i &lt; coins.length)</code> <code>coins[i]</code> is divisible by <code>coins[i - 1]</code>. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's <code>price</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>coins = [1, 2, 10]</code> and <code>price = 28</code>, the output should be<br>
<code>minimalNumberOfCoins(coins, price) = 6</code>.</p>
<p>You have to use <code>10</code> twice, and <code>2</code> four times.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer coins</strong></p>
<p>The coin values available in Bananaland.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ coins.length ≤ 5</code>,<br>
<code>1 ≤ coins[i] ≤ 120</code>.</p>
</li>
<li>
<p><strong>[input] integer price</strong></p>
<p>A positive integer representing the price of the banana.</p>
<p><em>Guaranteed constraints:</em><br>
<code>8 ≤ price ≤ 250</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimal number of coins you can use to buy the banana.</p>
</li>
</ul>
</div>