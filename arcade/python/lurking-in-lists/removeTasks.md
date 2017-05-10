<div class="markdown"><p>Today is a good day: it's the <code>k<sup>th</sup></code> year since you started to work at the company, which means you have to have a party today. In order to get home earlier and prepare for the jamboree, you need to get home early. You decided to remove each <code>k<sup>th</sup></code> tasks from your <code>toDo</code> list, since today is your day and you can do whatever you please.</p>
<p>Given the list of task ids in your <code>toDo</code> list, remove each <code>k<sup>th</sup></code> task from it and return the list of remaining tasks.</p>
<p><strong>Example</strong></p>
<p>For <code>k = 3</code> and <code>toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]</code>,<br>
the output should be<br>
<code>removeTasks(k, toDo) = [1237, 2847, 2947, 1, 374827, 22]</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 30</code>.</p>
</li>
<li>
<p><strong>[input] array.integer toDo</strong></p>
<p>Ids of the tasks in your to-do list.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ toDo.length ≤ 100</code>,<br>
<code>1 ≤ toDo[i] ≤ 4 · 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
</div>