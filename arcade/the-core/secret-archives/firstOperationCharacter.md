<div class="markdown"><p>Given a string which represents a valid arithmetic expression, find the index of the character in the given expression corresponding to the arithmetic operation which needs to be computed first.</p>
<p>Note that several operations of the same type with equal priority are computed from left to right.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>expr = "(2 + 2) * 2"</code>, the output should be<br>
<code>firstOperationCharacter(expr) = 3</code>.</p>
<p>There are two operations in the expression: <code>+</code> and <code>*</code>. The result of <code>+</code> should be computed first, since it is enclosed in parentheses. Thus, the output is the index of the <code>'+'</code> sign, which is <code>3</code>.</p>
</li>
<li>
<p>For <code>expr = "2 + 2 * 2"</code>, the output should be<br>
<code>firstOperationCharacter(expr) = 6</code>.</p>
<p>There are two operations in the given expression: <code>+</code> and <code>*</code>. Since there are no parentheses, <code>*</code> should be computed first as it has higher priority. The answer is the position of <code>'*'</code>, which is <code>6</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string expr</strong></p>
<p>A string consisting of digits, parentheses, addition and multiplication signs (pluses and asterisks). It is guaranteed that there is at least one arithmetic sign in it.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ expr.length ≤ 45</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>