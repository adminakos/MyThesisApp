<%--
  Created by IntelliJ IDEA.
  User: petro
  Date: 16/1/2020
  Time: 19:27
  To change this template use File | Settings | File Templates.
--%>
<%@ page import="java.util.*"%>
<%@ page import="java.io.*"%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>info</title>
</head>
<body>




<%

    String name = request.getParameter("uname");
    String data = request.getParameter("data");

    session.setAttribute("user", name);      //set attribute in session
    session.setAttribute("data", data);
    out.print("Welcome:  " + name);
    out.print("<br/><br/>");

    if (data.equals("oil")){
        out.print("  <p>The data contains daily Brent oil prices from 17th of May 1987 until the 30th of September 2019.</p>");

        out.print("  <p><h3>SOURCE:</h3> U.S. Energy Information Administration</p>");

        out.print("  <p><h3>UNITS:</h3>  Dollars per Barrel, Not Seasonally Adjusted</p>");

        out.print("  <p><h3>FREQUENCY:</h3>  Monthly</p>");

        out.print("  <p><h3>SUGGESTED CITATION:</h3>\n" +
                "U.S. Energy Information Administration, Crude Oil Prices: Brent - Europe [MCOILBRENTEU], retrieved from FRED, Federal Reserve Bank of St. Louis</p>");



    }else if (data.equals("unrate")){
        out.print("  <p>The unemployment rate represents the number of unemployed as a percentage of the labor force.\n"+
                "Labor force data are restricted to people 16 years of age and older, who currently reside in 1 of the 50 states or the District of Columbia,\n"+
                "who do not reside in institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.</p>");

        out.print("  <p><h3>SOURCE:</h3> U.S. Bureau of Labor Statistics</p>");

        out.print("  <p><h3>UNITS:</h3>  Percent, Seasonally Adjusted</p>");

        out.print("  <p><h3>FREQUENCY:</h3>  Monthly</p>");

        out.print("  <p><h3>SUGGESTED CITATION:</h3>\n" +
                "U.S. Bureau of Labor Statistics, Unemployment Rate [UNRATE], retrieved from FRED, Federal Reserve Bank of St. Louis</p>");


    }else if (data.equals("sales")){
        out.print("  <p>Total vehicle sales from 1976 to 2019.</p>");

        out.print("  <p><h3>SOURCE:</h3> U.S. Bureau of Economic Analysis</p>");

        out.print("  <p><h3>UNITS:</h3>  Millions of Units, Seasonally Adjusted Annual Rate</p>");

        out.print("  <p><h3>FREQUENCY:</h3>  Monthly</p>");

        out.print("  <p><h3>SUGGESTED CITATION:</h3>\n" +
                "U.S. Bureau of Economic Analysis, Total Vehicle Sales [TOTALSA], retrieved from FRED, Federal Reserve Bank of St. Louis</p>");



    }

%>
<form  align="center" method="post" action="session.jsp">
    <p> Click the button to visualize data set.</p>
    <input type="submit" value="Visualize">
</form>

</body>
</html>
