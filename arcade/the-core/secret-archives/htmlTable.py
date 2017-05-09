def htmlTable(html, row, col):
    try:
        html = html.split("<table>")[1].split("</table>")[0]
        html = "".join(html.split("<tr>", 1)[1].split("</tr>"))
        my_row = html.split("<tr>")[row]
        my_row = "".join(my_row.split("<td>", 1)[1].split("</td>"))
        return my_row.split("<td>")[col]
    except:
        return "No such cell"