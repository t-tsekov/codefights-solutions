<div class="markdown"><p>The web application service you're working on is supposed to be used by developers teams. To make the service more friendly, you'd like to implement a feature that will greet each person in a group.</p>
<p>Given a list of people in a <code>team</code>, return an array of greetings that should be printed out, where each greeting is in the format <code>"Hello, <em>&lt;team[i]&gt;</em>!"</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>team = ["Athos", "Porthos", "Aramis"]</code>,<br>
the output should be</p>
<pre><code>greetingsGenerator(team) = ["Hello, Athos!",
                            "Hello, Porthos!",
                            "Hello, Aramis!"]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string team</strong></p>
<p>A list of team members.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ team.length ≤ 10</code>,<br>
<code>1 ≤ team[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Array of strings, where the <code>i<sup>th</sup></code> string has the format <code>"Hello, <em>&lt;team[i]&gt;</em>!"</code>.</p>
</li>
</ul>
</div>