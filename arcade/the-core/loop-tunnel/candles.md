<div class="markdown"><p>When a candle finishes burning it leaves a leftover. <code>makeNew</code> leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.</p>
<p>You have <code>candlesNumber</code> candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?</p>
<p><strong>Example</strong></p>
<p>For <code>candlesNumber = 5</code> and <code>makeNew = 2</code>, the output should be<br>
<code>candles(candlesNumber, makeNew) = 9</code>.</p>
<p>Here is what you can do to burn <code>9</code> candles:</p>
<ul>
<li>burn <code>5</code> candles, obtain <code>5</code> leftovers;</li>
<li>create <code>2</code> more candles, using <code>4</code> leftovers (<code>1</code> leftover remains);</li>
<li>burn <code>2</code> candles, end up with <code>3</code> leftovers;</li>
<li>create another candle using <code>2</code> leftovers (<code>1</code> leftover remains);</li>
<li>burn the created candle, which gives another leftover (<code>2</code> leftovers in total);</li>
<li>create a candle from the remaining leftovers;</li>
<li>burn the last candle.</li>
</ul>
<p>Thus, you can burn <code>5 + 2 + 1 + 1 = 9</code> candles, which is the answer.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer candlesNumber</strong></p>
<p>The number of candles you have in your possession.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ candlesNumber ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] integer makeNew</strong></p>
<p>The number of leftovers that you can use up to create a new candle.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ makeNew ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>