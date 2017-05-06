<div class="markdown"><p>In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.</p>
<p>You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number <code>n</code> the <code>k<sup>th</sup></code> bit from the right was initially set to <code>0</code>, but its current value might be different. It's now up to you to write a function that will change the <code>k<sup>th</sup></code> bit of <code>n</code> back to <code>0</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 37</code> and <code>k = 3</code>, the output should be<br>
<code>killKthBit(n, k) = 33</code>.</p>
<p><code>37<sub>10</sub> = 100<b><font color="red">1</font></b>01<sub>2</sub> ~&gt; 100<b><font color="red">0</font></b>01<sub>2</sub> = 33<sub>10</sub></code>.</p>
</li>
<li>
<p>For <code>n = 37</code> and <code>k = 4</code>, the output should be<br>
<code>killKthBit(n, k) = 37</code>.</p>
<p>The <code>4<sup>th</sup></code> bit is <code>0</code> already (looks like the Mad Coder forgot to encrypt this number), so the answer is still <code>37</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ n ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The 1-based index of the changed bit (counting from the right).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 31</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>