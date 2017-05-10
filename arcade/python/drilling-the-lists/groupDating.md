<div class="markdown"><p>You're organizing a group dating activity for cats, i.e. a meeting where an equal number of <code>male</code> and <code>female</code> cats get together. For each cat you calculate their <em>nature value</em>, an integer that describes the cat's spirit. When a male and a female cat with the same <em>nature value</em> see each other, they become connected and happily walk out together.</p>
<p>You've just started another group dating, and placed the cats in front of one another so that the <code>i<sup>th</sup></code> male is sitting across the <code>i<sup>th</sup></code> female. What cats will remain at their places, assuming that the pairs of cats sitting in front of each other and having the same <em>nature values</em> will walk out?</p>
<p><strong>Example</strong></p>
<p>For <code>male = [5, 28, 14, 99, 17]</code> and<br>
<code>female = [5, 14, 28, 99, 16]</code>,<br>
the output should be<br>
<code>groupDating(male, female) = [[28, 14, 17], [14, 28, 16]]</code>.</p>
<p>Pairs of cats at positions <code>0</code> and <code>3</code> (0-based) have the same <em>nature values</em>, so they will leave the meeting.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer male</strong></p>
<p><em>Nature values</em> of male cats.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ male.length ≤ 20</code>,<br>
<code>0 ≤ male[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.integer female</strong></p>
<p><em>Nature values</em> of female cats.</p>
<p><em>Guaranteed constraints:</em><br>
<code>female.length = male.length</code>,<br>
<code>0 ≤ female[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A list of two elements, where the first element will contain <em>nature values</em> of the remaining male cats, and the second element will contain <em>nature values</em> of the remaining female cats. In both cases, the values should go in the order the corresponding cats are sitting.</p>
<p><em>Note</em>: if your solution returns a list of tuples, the tuples will be converted to list automatically.</p>
</li>
</ul>
</div>