<div class="markdown"><p>Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>inputArray = ["aba", "bbb", "bab"]</code>, the output should be<br>
<code>stringsRearrangement(inputArray) = false</code>;</p>
<p>All rearrangements don't satisfy the description condition.</p>
</li>
<li>
<p>For <code>inputArray = ["ab", "bb", "aa"]</code>, the output should be<br>
<code>stringsRearrangement(inputArray) = true</code>.</p>
<p>Strings can be rearranged in the following way: <code>"aa", "ab", "bb"</code>.<br>
<strong>Input/Output</strong></p>
</li>
</ul>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string inputArray</strong></p>
<p>A non-empty array of strings of lowercase letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ inputArray.length ≤ 10</code>,<br>
<code>1 ≤ inputArray[i].length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>