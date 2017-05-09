<div class="markdown"><p>Whenever you decide to celebrate your birthday you always do this your favorite café, which is quite popular and as such usually very crowded. This year you got lucky: when you and your friend enter the café you're surprised to see that it's almost empty. The waiter lets slip that there are always very few people on this day of the week.</p>
<p>You enjoyed having the café all to yourself, and are now curious about the next time you'll be this lucky. Given the current <code>birthdayDate</code>, determine the number of years until it will fall on the same day of the week.</p>
<p>For your convenience, here is the list of months lengths (from January to December, respectively):</p>
<ul>
<li>Months lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap">leap years</a> February has <code>29</code> days. If your birthday is on the <code>29<sup>th</sup></code> of February, you celebrate it once in four years. Otherwise you birthday is celebrated each year.</p>
<p><strong>Example</strong></p>
<p>For <code>birthdayDate = "02-01-2016"</code>, the output should be<br>
<code>dayOfWeek(birthdayDate) = 5</code>.</p>
<p>February 1 in <code>2016</code> is a Monday. The next year in which this same date will be Monday too is <code>2021</code>. <code>2021 - 2016 = 5</code>, which is the answer.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string birthdayDate</strong></p>
<p>A string representing the correct date in the format <code>mm-dd-yyyy</code>, where <code>mm</code> is the number of month (1-based, i.e. <code>01</code> for January, <code>02</code> for February and so on), <code>dd</code> is the day, and <code>yyyy</code> is the year.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ int(mm) ≤ 12</code>,<br>
<code>1 ≤ int(dd) ≤ 31</code>,<br>
<code>1900 ≤ int(yyyy) ≤ 2100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>An integer describing the number of years until your birthday falls on the same day of the week.</p>
</li>
</ul>
</div>