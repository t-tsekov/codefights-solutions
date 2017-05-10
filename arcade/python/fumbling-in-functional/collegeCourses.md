<div class="markdown"><p>John has just entered a college, and should now pick several courses to take. He knows nothing, except that number <code>x</code> is a bad luck for him, which is why he won't even consider courses whose title consist of <code>x</code> letters.</p>
<p>Given a list of <code>courses</code>, remove the courses with titles consisting of <code>x</code> letters and return the result.</p>
<p><strong>Example</strong></p>
<p>For <code>x = 7</code> and<br>
<code>courses = ["Art", "Finance", "Business", "Speech", "History", "Writing", "Statistics"]</code>,<br>
the output should be<br>
<code>collegeCourses(x, courses) = ["Art", "Business", "Speech", "Statistics"]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer x</strong></p>
<p>John's unlucky number.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ x ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] array.string courses</strong></p>
<p>The list of courses.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ courses.length ≤ 50</code>,<br>
<code>3 ≤ courses[i].length ≤ 25</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The courses John should consider.</p>
</li>
</ul>
</div>