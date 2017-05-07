<div class="markdown"><p>There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house <em>sorted in ascending order</em>. It's guaranteed that each person has <code>2</code> legs and each cat has <code>4</code> legs.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>legs = 6</code>, the output should be<br>
<code>houseOfCats(legs) = [1, 3]</code>.</p>
<p>There could be either <code>1</code> cat and <code>1</code> person (<code>4 + 2 = 6</code>) or <code>3</code> people (<code>2 * 3 = 6</code>).</p>
</li>
<li>
<p>For <code>legs = 2</code>, the output should be<br>
<code>houseOfCats(legs) = [1]</code>.</p>
<p>There can be only <code>1</code> person.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer legs</strong></p>
<p>The total number of legs in the house.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ legs ≤ 45</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Every possible number of people that can be in the house.</p>
</li>
</ul>
</div>