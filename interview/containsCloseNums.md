<div class="markdown"><p>Given an array of integers <code>nums</code> and an integer <code>k</code>, determine whether there are two distinct indices <code>i</code> and <code>j</code> in the array where <code>nums[i] = nums[j]</code> and the absolute difference between <code>i</code> and <code>j</code> is less than or equal to <code>k</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>nums = [0, 1, 2, 3, 5, 2]</code> and <code>k = 3</code>, the output should be<br>
<code>containsCloseNums(nums, k) = true</code>.</p>
<p>There are two <code>2</code>s in <code>nums</code>, and the absolute difference between their positions is exactly <code>3</code>.</p>
</li>
<li>
<p>For <code>nums = [0, 1, 2, 3, 5, 2]</code> and <code>k = 2</code>, the output should be<br><br>
<code>containsCloseNums(nums, k) = false</code>.</p>
<p>The absolute difference between the positions of the two <code>2</code>s is <code>3</code>, which is more than <code>k</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer nums</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ nums.length ≤ 55000</code>,<br>
<code>-2<sup>31</sup> - 1 ≤ nums[i] ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ k ≤ 35000</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
</div>