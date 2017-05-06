<div class="markdown"><p>We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non <code>0</code> digit of the number and round it to <code>0</code> or to <code>10</code>. If it's less than <code>5</code> we round it to <code>0</code> if it's larger than or equal to <code>5</code> we round it to <code>10</code> (rounding to <code>10</code> means increasing the next significant digit by <code>1</code>). The process stops immediately once there is only one non-zero digit left.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>value = 15</code>, the output should be<br>
<code>rounders(value) = 20</code>;</p>
</li>
<li>
<p>For <code>value = 1234</code>, the output should be<br>
<code>rounders(value) = 1000</code>.</p>
<p><code>1234 -&gt; 1230 -&gt; 1200 -&gt; 1000</code>.</p>
</li>
<li>
<p>For <code>value = 1445</code>, the output should be<br>
<code>rounders(value) = 2000</code>.</p>
<p><code>1445 -&gt; 1450 -&gt; 1500 -&gt; 2000</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer value</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ value ≤ 10<sup>8</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The rounded number.</p>
</li>
</ul>
</div>