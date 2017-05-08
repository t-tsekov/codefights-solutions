<div class="markdown"><p>Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:</p>
<ul>
<li><em>type</em> indicates if it's a left or a right shoe;</li>
<li><em>size</em> is the size of the shoe.</li>
</ul>
<p>Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
</code></pre>
<p>the output should be<br>
<code>pairOfShoes(shoes) = true</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [1, 23]]
</code></pre>
<p>the output should be<br>
<code>pairOfShoes(shoes) = false</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer shoes</strong></p>
<p>Array of shoes. Each shoe is given in the format <code>[<em>type</em>, <em>size</em>]</code>, where <em>type</em> is either <code>0</code> or <code>1</code> for left and right respectively, and <em>size</em> is a positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ shoes.length ≤ 25</code>,<br>
<code>1 ≤ shoes[i][1] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if it is possible to pair the shoes, <code>false</code> otherwise.</p>
</li>
</ul>
</div>