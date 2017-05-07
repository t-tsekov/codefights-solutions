<div class="markdown"><p>Given a positive integer number and a certain length, we need to modify the given number to have a specified length. We are allowed to do that either by cutting out leading digits (if the number needs to be shortened) or by adding <code>0s</code> in front of the original number.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>number = 1234</code> and <code>width = 2</code>, the output should be<br>
<code>integerToStringOfFixedWidth(number, width) = "34"</code>;</li>
<li>For <code>number = 1234</code> and <code>width = 4</code>, the output should be<br>
<code>integerToStringOfFixedWidth(number, width) = "1234"</code>;</li>
<li>For <code>number = 1234</code> and <code>width = 5</code>, the output should be<br>
<code>integerToStringOfFixedWidth(number, width) = "01234"</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer number</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ number ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer width</strong></p>
<p>A positive integer representing the desired length.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ width ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The modified version of <code>number</code> as described above.</p>
</li>
</ul>
</div>