'<div class="markdown"><p>Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about to go viral. You cannot let this ruin your reputation, so you want to apply <em>box blur</em> algorithm to the photo to hide its content.</p>
<p>The algorithm works as follows: each pixel <code>x</code> in the resulting image has a value equal to the average value of the input image pixels' values from the <code>3 × 3</code> square with the center at <code>x</code>. All pixels at the edges are cropped.</p>
<p>As pixel's value is an integer, all fractions should be rounded down.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
</code></pre>
<p>the output should be <code>boxBlur(image) = [[1]]</code>.</p>
<p>In the given example all boundary pixels were cropped, and the value of the pixel in the middle was obtained as <code>(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = <em>~rounded down~</em> = 1</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.integer image</strong></p>
<p>An image is stored as a rectangular matrix of non-negative integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ image.length ≤ 10</code>,<br>
<code>3 ≤ image[0].length ≤ 10</code>,<br>
<code>0 ≤ image[i][j] ≤ 255</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A blurred image.</p>
</li>
</ul>
</div>'