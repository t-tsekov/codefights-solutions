<div class="markdown"><p>Given an array of integers, determine whether there are two distinct indices <code>i</code> and <code>j</code> in the array such that:</p>
<ul>
<li>The absolute difference between <code>i</code> and <code>j</code> is at most <code>k</code></li>
<li>The absolute difference between <code>nums[i]</code> and <code>nums[j]</code> is at most <code>t</code></li>
</ul>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>nums = [1, 3, 1]</code>, <code>k = 2</code> and <code>t = 1</code>, the output should be<br>
<code>containsNearbyAlmostDuplicate(nums, k, t) = true</code>.</p>
<p>The absolute difference between indices <code>0</code> and <code>2</code> is <code>2</code> (the value of <code>k</code>) and the absolute difference between elements <code>1</code> and <code>1</code> is <code>0</code> (less than the value of <code>t</code>), so this array meets all of the requirements and the output is <code>true</code>.</p>
</li>
<li>
<p>For <code>nums = [-3, 3]</code>, <code>k = 2</code> and <code>t = 4</code>, the output should be<br>
<code>containsNearbyAlmostDuplicate(nums, k, t) = false</code>.</p>
<p>The absolute difference between <code>-3</code> and <code>3</code> is <code>6</code>, which is more than the value of <code>t</code>, meaning that the output is <code>false</code>.</p>
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
<code>2 ≤ nums.length ≤ 2 · 10<sup>5</sup></code>,<br>
<code>-2<sup>31</sup>≤ nums[i] ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>An integer that represents the highest allowable absolute difference between <code>i</code> and <code>j</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer t</strong></p>
<p>An integer that represents the highest allowable absolute difference between <code>nums[i]</code> and <code>nums[j]</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ t ≤ 2<sup>31</sup> - 1</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if the input array meets the requirements as stated above, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>