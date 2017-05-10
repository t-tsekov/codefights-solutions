<div class="markdown"><p>A 2D list <code>lst</code> of size <code>2 * n - 1</code> is called a <em>shell</em> if it is filled with zeros and has the following configuration:</p>
<ul>
<li><code>lst[0]</code> contains one element;</li>
<li><code>lst[1]</code> contains two elements;</li>
<li>...</li>
<li><code>lst[n - 2]</code> contains <code>n - 1</code> elements;</li>
<li><code>lst[n - 1]</code> contains <code>n</code> elements;</li>
<li><code>lst[n]</code> contains <code>n - 1</code> elements;</li>
<li>...</li>
<li><code>lst[2 * n - 3]</code> contains two elements;</li>
<li><code>lst[2 * n - 2]</code> contains one element.</li>
</ul>
<p>Given an integer <code>n</code>, return a <em>shell</em> list.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 3</code>, the output should be</p>
<pre><code>constructShell(n) = [[0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 0],
                     [0]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>An integer defining the size of the <em>shell</em>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 30</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A <em>shell</em>.</p>
</li>
</ul>
</div>