<div class="markdown"><p>Given an array <code>strings</code>, determine whether it follows the sequence given in the <code>patterns</code> array. In other words, there should be no <code>i</code> and <code>j</code> for which <code>strings[i] = strings[j]</code> and <code>patterns[i] ≠ patterns[j]</code> or for which <code>strings[i] ≠ strings[j]</code> and <code>patterns[i] = patterns[j]</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>strings = ["cat", "dog", "dog"]</code> and <code>patterns = ["a", "b", "b"]</code>, the output should be<br>
<code>areFollowingPatterns(strings, patterns) = true</code>;</li>
<li>For <code>strings = ["cat", "dog", "doggy"]</code> and <code>patterns = ["a", "b", "b"]</code>, the output should be<br>
<code>areFollowingPatterns(strings, patterns) = false</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string strings</strong></p>
<p>An array of strings, each containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ strings.length ≤ 10<sup>5</sup></code>,<br>
<code>1 ≤ strings[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.string patterns</strong></p>
<p>An array of pattern strings, each containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>patterns.length = strings.length</code>,<br>
<code>1 ≤ patterns[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if <code>strings</code> follows <code>patterns</code> and <code>false</code> otherwise.</p>
</li>
</ul>
</div>