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

    <%


        String data =(String) session.getAttribute("data");

//    session.setAttribute("user", name);      //set attribute in session
//    out.print("<br/>hhhhhhhhhhhhhhhhhhhhhhhhhhh<br/>");

        if (data.equals("oil")){

//        out.print("<br/>bbbbb<br/>");
            try{
                String s = null;

                Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\Oil_betteralgo.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while((s = in.readLine())!= null){
                    out.print(s+"<br/<br/>");

                }
            }catch(Exception e) {
                e.printStackTrace();
            }


        }else if (data.equals("unrate")){


            try{
                String s = null;

                Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\Unempl_betteralgo.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while((s = in.readLine())!= null){
                    out.print(s+"<br/<br/>");

                }
            }catch(Exception e) {
                e.printStackTrace();
            }
        }else if (data.equals("sales")){


            try{
                String s = null;

                Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\Sales_betteralgo.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while((s = in.readLine())!= null){
                    out.print(s+"<br/<br/>");

                }
            }catch(Exception e) {
                e.printStackTrace();
            }

        }

    %>

</form>


</body>
</html>