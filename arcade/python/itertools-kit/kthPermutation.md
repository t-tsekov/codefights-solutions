<div class="markdown"><p>You found your old bike in the attic, and would love to refresh your childhood memories and give it a ride. Unfortunately there is a chain lock on the bike, and the code is a permutation of a set of distinct <code>numbers</code>. Of course, you don't remember it after all these years.</p>
<p>You do remember, however, that the last time you picked up your bike you also couldn't remember the code, so had to run over all possible <code>numbers</code> permutations. Being a programmer, you tried them in the <a href="keyword://lexicographical-order-for-permutations">lexicographical order</a>. It took you a couple of days, and in the first day you managed to check <code>k - 1</code> permutations.</p>
<p>Now that you need to open the lock again, you can start checking the permutations from the <code>k<sup>th</sup></code> one. Given the list of <code>numbers</code>, return the <code>k<sup>th</sup></code> (1-based) permutation that you should begin with.</p>
<p><strong>Example</strong></p>
<p>For <code>numbers = [1, 2, 3, 4, 5]</code> and <code>k = 4</code>, the output should be<br>
<code>kthPermutation(numbers, k) = [1, 2, 4, 5, 3]</code>.</p>
<p>Here are the first <code>4</code> permutations:</p>
<ul>
<li><code>[1, 2, 3, 4, 5]</code></li>
<li><code>[1, 2, 3, 5, 4]</code></li>
<li><code>[1, 2, 4, 3, 5]</code></li>
<li><code>[1, 2, 4, 5, 3]</code></li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer numbers</strong></p>
<p>A sorted list of distinct integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ numbers.length ≤ 10</code>,<br>
<code>1 ≤ numbers[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The 1-based index of the first permutation that you should try.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ numbers.length!</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The <code>k<sup>th</sup></code> permutation of <code>numbers</code>.</p>
<p><em>Note</em>: if your solution returns a tuple, it will be converted to list automatically.</p>
</li>
</ul>
</div>