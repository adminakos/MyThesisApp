<%--
  Created by IntelliJ IDEA.
  User: petro
  Date: 13/1/2020
  Time: 15:36
  To change this template use File | Settings | File Templates.
--%>

<%@ page import="java.util.*"%>
<%@ page import="java.io.*"%>


<html>
  <head>

      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ThesisAPP</title>
  </head>
  <body>


        <form align="center" action="info.jsp">


                <h1>ENTER YOUR NAME</h1>
            Name  : <input type="text" name="uname">

                <h3>PLEASE CHOOSE DATA SET TO VISUALIZE</h3>

                <!--  <input type="file" id="upload" name="upload"  multiple />-->

        <!-- < a href="" onclick="document.getElementById('upload').click(); return false">Upload File</a>-->

                    <!--<input type="submit" value="Click"><br/>-->

                     <select name="data">
        <option value="oil">Crude Oil Prices Brent - Europe</option>
        <option value="sales">Total Vehicle Sales</option>
        <option value="unrate">Unemployment Rate</option>
    </select>
    <p> Click the button for data set information.</p>
    <input type="submit" value="Info">
</form>


  </body>
</html>
