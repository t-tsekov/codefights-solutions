<div class="markdown"><p>Consider two straight lines given as <code>y = mx + b</code>. You forgot what they mean but you're sure that the destiny of the universe depends on them. To save the world, you have to choose one of these lines. Here is how to make the proper choice:</p>
<ul>
<li>Consider all integer coordinates <code>a</code> for all possible values of <code>a</code> from <code>l</code> to <code>r</code>, inclusive.</li>
<li>For each vertical <code>x = a</code>, find the points where this vertical intersects with <code>line1</code> and <code>line2</code>. Denote these points as <code>p1</code> and <code>p2</code>, respectively. If <code>p1</code> and <code>p2</code> don't coincide, give one point to the line which is higher in that vertical.</li>
<li>Choose the line which has a larger score. Return <code>"first"</code> for <code>line1</code>, <code>"second"</code> for <code>line2</code> and <code>"any"</code> if both lines have the same score.</li>
</ul>
<p><strong>Example</strong></p>
<ul>
<li>For <code>line1 = [1, 2]</code>, <code>line2 = [2, 1]</code>, <code>l = 0</code> and <code>r = 2</code>, the output should be<br>
<code>twoLines(line1, line2, l, r) = "any"</code>;</li>
<li>For <code>line1 = [1, 2]</code>, <code>line2 = [2, 1]</code>, <code>l = -1</code> and <code>r = 2</code>, the output should be<br>
<code>twoLines(line1, line2, l, r) = "first"</code>;</li>
<li>For <code>line1 = [1, 2]</code>, <code>line2 = [2, 1]</code>, <code>l = 0</code> and <code>r = 3</code>, the output should be<br>
<code>twoLines(line1, line2, l, r) = "second"</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer line1</strong></p>
<p>An array containing two integers, <code>m</code> and <code>b</code>, respectively. These integers correspond to line equation coefficients.</p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ line1[i] ≤ 1000</code><br>
<code>line1[0] * line1[1] ≠ 0</code></p>
</li>
<li>
<p><strong>[input] array.integer line2</strong></p>
<p>An array in the same format as <code>line1</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ line2[i] ≤ 1000</code><br>
<code>line2[0] * line2[1] ≠ 0</code></p>
</li>
<li>
<p><strong>[input] integer l</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ l ≤ r ≤ 1000</code></p>
</li>
<li>
<p><strong>[input] integer r</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>-1000 ≤ l ≤ r ≤ 1000</code></p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
</div>