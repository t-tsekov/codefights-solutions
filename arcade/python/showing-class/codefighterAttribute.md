<div class="markdown"><p>At CodeFights information about the CodeFighters is stored in the database. Anny is working on the class representation of this information, and needs to come up with a class that creates objects with the following attributes: <code>username</code>, <code>_id</code>, <code>xp</code> and <code>name</code>. She has already come up with a test object:</p>
<pre><code>username: "annymaster"
_id: "1234567"
xp: "1500"
name: "anny"
</code></pre>
<p>The problem is, she doesn't know if this will be enough. It is possible that the server will require information about additional attributes that are not yet present in Anny's representation.</p>
<p>Given the <code>attribute</code> the server requested, return its value if it is defined, and the <code><em>&lt;attribute&gt;</em> attribute is not defined</code> string otherwise.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>attribute = "_id"</code>, the output should be<br>
<code>codefighterAttribute(attribute) = "1234567"</code>;</p>
</li>
<li>
<p>For <code>attribute = "age"</code>, the output should be<br>
<code>codefighterAttribute(attribute) = "age attribute is not defined"</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string attribute</strong></p>
<p>An attribute the server requested.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ attribute.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The value of the attribute if it's defined, <code><em>&lt;attribute&gt;</em> attribute is not defined</code> otherwise.</p>
</li>
</ul>
</div>