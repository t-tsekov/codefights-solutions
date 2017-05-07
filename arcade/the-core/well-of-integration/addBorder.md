<div class="markdown"><p>Given a rectangular matrix of characters, add a border of asterisks(<code>*</code>) to it.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>picture = ["abc",
           "ded"]
</code></pre>
<p>the output should be</p>
<pre><code>addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string picture</strong></p>
<p>A non-empty array of non-empty equal-length strings.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ picture.length ≤ 5</code>,<br>
<code>1 ≤ picture[i].length ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The same matrix of characters, framed with a border of asterisks of width <code>1</code>.</p>
</li>
</ul>
</div>