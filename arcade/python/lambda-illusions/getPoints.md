<div class="markdown"><p>A new scoring system was introduced in your university: from now on, each test will consist of the predefined list of questions, and for the <code>i<sup>th</sup></code> (1-based) question a student either gets <code>i</code> points, or loses <code>p</code> points as a penalty.</p>
<p>Your task is to calculate the number of points a student got for some test. Implement a function that would calculate the number of points received for the test based on the given list of <code>answers</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>answers = [true, true, false, true]</code>and <code>p = 2</code>, the output should be<br>
<code>getPoints(answers, p) = 5</code>.</p>
<p>Here's why: <code>1 + 2 - 2 + 4 = 5</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.boolean answers</strong></p>
<p>Array of student's answers. <code>answers[i]</code> is <code>true</code> if the student answered the <code>(i + 1)<sup>th</sup></code> question correctly, and <code>false</code> otherwise.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ answers.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer p</strong></p>
<p>The number of points subtracted from the final score for each incorrect result.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ p ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of points the student received for the test.</p>
</li>
</ul>
</div>