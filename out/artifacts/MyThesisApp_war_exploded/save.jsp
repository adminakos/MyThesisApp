<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.InputStreamReader" %>
<%@ page import="java.io.BufferedWriter" %>
<%@ page import="java.io.FileWriter" %>
<%@ page import ="java.io.FileNotFoundException"%>
<%@ page import = "java.io.FileReader"%>
<%@ page import = "java.io.IOException"%>
<%@ page import="java.util.Arrays" %><%--
  Created by IntelliJ IDEA.
  User: petro
  Date: 14/1/2020
  Time: 19:13
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%--<%@page contentType="text/html" pageEncoding="UTF-8"%>--%>
<!DOCTYPE html>
<html>
<head>
    <%--<script type="text/javascript">--%>
    <%--function myFunction() {--%>
    <%--var x = document.getElementById("myTextarea").value;--%>
    <%--document.getElementById("demo").innerHTML = x;--%>
    <%--var y = new String(x);--%>
    <%--document.location.href ="session.jsp?atr="+y;--%>
    <%--}--%>
    <%--</script>--%>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ThesisAPP</title>
</head>
<body>

<form align="center">

<%String text = (String) request.getParameter("text");
    System.out.println(text);
    String[] values = text.split(",");
    System.out.println(Arrays.toString(values));
    BufferedWriter br = new BufferedWriter(new FileWriter("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv"));
    StringBuilder sb = new StringBuilder();

// Append strings from array
    for (String element : values) {
        sb.append(element);
        sb.append("\n");
    }

    br.write(sb.toString());
    br.close();
%>
</form>
<form align = "center" action="session3.jsp">
    <h4> Choose one of the following algorithms to visualize anomallies.</h4>
    <select align="center" name="item">
        <option value="svm">ONE CLASS SVM</option>
        <option value="islforest">ISOLATION FOREST</option>
        <option value="kmeans">KMEANS</option>
        <option value="sax">S.A.X.</option>
        <option value="all">ALL of them</option>
    </select>



    <input type="submit" value="Anomalies">
</form>
</body>
</html>

<%--out.print("<br/>Write anomalous Values separated with comma: <br/>");--%>
<%--out.print("<textarea name=\"text\" id=\"myTextarea\" rows="+5+" cols="+50+">");--%>
<%--out.print("</textarea>");--%>

<%--out.print("<button type=\"button\" onclick=\"myFunction()\">Submit</button>");--%>

<%--<form align = "center" action="session3.jsp">--%>
<%--<h4> Choose one of the following algorithms to visualize anomallies.</h4>--%>
<%--<select align="center" name="item">--%>
<%--<option value="svm">ONE CLASS SVM</option>--%>
<%--<option value="islforest">ISOLATION FOREST</option>--%>
<%--<option value="kmeans">KMEANS</option>--%>
<%--<option value="sax">S.A.X.</option>--%>
<%--<option value="all">ALL of them</option>--%>
<%--</select>--%>



<%--<input type="submit" value="Anomalies">--%>
<%--</form>--%>
