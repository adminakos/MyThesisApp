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
    <title>THESIS</title>
  </head>
  <body>


        <form action="session.jsp">
            <pre>

                <h1>ENTER YOUR NAME</h1>
            Name  : <input type="text" name="uname">


                <h2>PLEASE CHOOSE DATA SET TO UPLOAD</h2>

                 <input type="file" id="upload" name="upload"  multiple />

        <!-- < a href="" onclick="document.getElementById('upload').click(); return false">Upload File</a>--!>

                    <input type="submit" value="Click"><br/>
</pre>
        </form>



  </body>
</html>
