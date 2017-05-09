<div class="markdown"><p>You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.</p>
<p><strong>Example</strong></p>
<p>For <code>part = "02:20:00"</code> and <code>total = "07:00:00"</code>, the output should be<br>
<code>videoPart(part, total) = [1, 3]</code>.</p>
<p>You have watched <code>1 / 3</code> of the whole video.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string part</strong></p>
<p>A string of the following format <code>"hh:mm:ss"</code> representing the time you have been watching the video.</p>
</li>
<li>
<p><strong>[input] string total</strong></p>
<p>A string of the following format <code>"hh:mm:ss"</code> representing the total video duration.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of the following format <code>[a, b]</code> (where <code>a / b</code> is <a href="keyword://reduced-fraction">a reduced fraction</a>).</p>
</li>
</ul>
</div>