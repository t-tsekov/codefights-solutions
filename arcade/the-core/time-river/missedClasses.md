<div class="markdown"><p>Your Math teacher takes education very seriously, and hates it when a class is missed or canceled for any reason. He even made up the following rule: if a class is missed because of a holiday, the teacher will compensate for it with a makeup class after school.</p>
<p>You're given an array, <code>daysOfTheWeek</code>, with the weekdays on which your teacher's classes are scheduled, and <code>holidays</code>, representing the dates of the holidays throughout the academic year (from <code>1<sup>st</sup></code> of September in <code>year</code> to <code>31<sup>st</sup></code> of May in <code>year + 1</code>). How many times will you be forced to stay after school for a makeup class because of holiday conflicts in the current academic year?</p>
<p>For your convenience, here is the list of month lengths (from January to December, respectively):</p>
<ul>
<li>Month lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please note that in <a href="keyword://leap">leap years</a> February has <code>29</code> days.</p>
<p><strong>Example</strong></p>
<p>For <code>year = 2015</code>, <code>daysOfTheWeek = [2, 3]</code> and<br>
<code>holidays = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"]</code>,<br>
the output should be<br>
<code>missedClasses(year, daysOfTheWeek, holidays) = 3</code>.</p>
<p>November <code>4<sup>th</sup></code> of <code>2015</code> is a Wednesday, February <code>23<sup>th</sup></code> of <code>2016</code> and March <code>8<sup>th</sup></code> of <code>2016</code> are Tuesdays, and the other holidays fall on Mondays. Classes are scheduled on Wednesdays and Tuesdays, so there will be only <code>3</code> missed classes.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer year</strong></p>
<p>An integer representing the correct year. The current academic year started on September <code>1</code>st and will finish on May <code>31</code>st of <code>year + 1</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1900 ≤ year ≤ 2100</code>.</p>
</li>
<li>
<p><strong>[input] array.integer daysOfTheWeek</strong></p>
<p>A sorted array of integers from <code>1</code> to <code>7</code> representing the days of the week (1-based, i.e. <code>1</code> for Monday, <code>2</code> for Tuesday and so on) on which classes are scheduled.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ daysOfTheWeek.length ≤ 7</code>,<br>
<code>1 ≤ daysOfTheWeek[i] ≤ 7</code>.</p>
</li>
<li>
<p><strong>[input] array.string holidays</strong></p>
<p>An array of strings representing the correct dates of holidays in this academic year in the format <code>"mm-dd"</code>, where <code>"mm"</code> stands for the month (1-based, i.e. <code>"01"</code> for January, <code>"02"</code> for February and so on) and <code>"dd"</code> stands for the day.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ holidays.length ≤ 30</code>,<br>
<code>1 ≤ int(mm) ≤ 12</code>, except <code>6</code>, <code>7</code> and <code>8</code>,<br>
<code>1 ≤ int(dd) ≤ 31</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of classes that will be missed.</p>
</li>
</ul>
</div>