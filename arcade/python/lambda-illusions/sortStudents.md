<div class="markdown"><p>You are given a list of <code>students</code> who want to apply to the internship at CodeFights. For the <code>i<sup>th</sup></code> student you know their full name <code>students[i]</code>, which can consist of up to <code>5</code> words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.</p>
<p>Your task is to sort the students <a href="keyword://lexicographical-order-for-strings">lexicographically</a> by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]
</code></pre>
<p>the output should be</p>
<pre><code>sortStudents(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string students</strong></p>
<p>Array of students, where each student is given by their full name consisting of at most <code>5</code> words. For each <code>i</code> <code>students[i]</code> consists of English letters and whitespace (<code>' '</code>) characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ students.length ≤ 30</code>,<br>
<code>1 ≤ students[i].length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Array of <code>students</code> sorted as described above.</p>
</li>
</ul>
</div>