<%--
  Created by IntelliJ IDEA.
  User: petro
  Date: 14/1/2020
  Time: 19:13
  To change this template use File | Settings | File Templates.
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>JSP Page</title>
</head>
<body>


<%

    String name = request.getParameter("uname");

    out.print("Welcome " + name);


    session.setAttribute("user", name);      //set attribute in session



%>
<a href = "session2.jsp">Next Page</a>
</body>
</html>