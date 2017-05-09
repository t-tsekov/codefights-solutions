<div class="markdown"><p>Benjamin recently bought a digital clock at a magic trick shop. The seller never told Ben what was so special about it, but mentioned that one day Benjamin would be faced with a surprise.</p>
<p>Indeed, the clock did surprise Benjamin: without warning, at <code>someTime</code> the clock suddenly started going in the opposite direction! Unfortunately, Benjamin has an important meeting very soon, and knows that at <code>leavingTime</code> he should leave the house so as to not be late. Ben spent all his money on the clock, so has to figure out what time his clock will show when it's time to leave.</p>
<p>Given the <code>someTime</code> at which the clock started to go backwards, find out what time will be shown on the curious clock at <code>leavingTime</code>.</p>
<p>For your convenience, here is the list of months lengths (from January to December, respectively):</p>
<ul>
<li>Months lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap">leap years</a> February has <code>29</code> days.</p>
<p><strong>Example</strong></p>
<p>For <code>someTime = "2016-08-26 22:40"</code> and <code>leavingTime = "2016-08-29 10:00"</code>, the output should be<br>
<code>curiousClock(someTime, leavingTime) = "2016-08-24 11:20"</code>.</p>
<p>There are <code>2</code> days, <code>11</code> hours and <code>20</code> minutes till the meeting. Thus, the clock will show <code>2016-08-24 11:20</code> at the <code>leavingTime</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string someTime</strong></p>
<p>The time at which the clock started going backwards. It is guaranteed that the time is correct and is not earlier than the midnight of January the 1<sup>st</sup>, 1970.</p>
<p>The time is given in the format <code>"YYYY-MM-DD HH:MM"</code>.</p>
</li>
<li>
<p><strong>[input] string leavingTime</strong></p>
<p>The time at which Ben will have to leave for the meeting in the same format as <code>someTime</code> and with the same constraints.<br>
It is guaranteed that <code>leavingTime</code> is later than <code>someTime</code>, but not later than the year of <code>2035</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The time Ben's curious clock will show when it's time to leave in the same format as <code>leavingTime</code> and <code>someTime</code>. It is guaranteed that it will be not earlier than the midnight of January the 1<sup>st</sup>, 1970.</p>
</li>
</ul>
</div>