<div class="markdown"><p><em>Avoid using C++'s <code>std::next_permutation</code> or similar features in other languages to solve this challenge. Implement the algorithm yourself, since this is what you would be asked to do during a real interview.</em></p>
<p>Given a string <code>s</code>, find all its potential permutations. The output should be sorted in <a href="keyword://lexicographical-order-for-strings">lexicographical order</a>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>s = "CBA"</code>, the output should be<br>
<code>stringPermutations(s) = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]</code>;</li>
<li>For <code>s = "ABA"</code>, the output should be<br>
<code>stringPermutations(s) = ["AAB", "ABA", "BAA"]</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string containing only capital letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>All permutations of <code>s</code>, sorted in lexicographical order.</p>
</li>
</ul>
</div>