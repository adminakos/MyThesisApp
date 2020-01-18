<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.InputStreamReader" %><%--
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
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ThesisAPP</title>
</head>
<body>



<%


    String data =(String) session.getAttribute("data");

//    session.setAttribute("user", name);      //set attribute in session
    out.print("<br/>hhhhhhhhhhhhhhhhhhhhhhhhhhh<br/>");

    if (data.equals("oil")){

        out.print("<br/>bbbbb<br/>");
        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\vizualiseOil.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }else if (data.equals("unrate")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\vizualiseUnempl.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }
    }else if (data.equals("sales")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\vizualise.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }

%>


<form action="session3.jsp">
    <h4> Choose one of the following algorithms to visualize anomallies.</h4>
    <select align="center" name="item">
        <option value="svm">ONE CLASS SVM</option>
        <option value="islforest">ISOLATION FOREST</option>
        <option value="sax">S.A.X.</option>
        <option value="all">ALL of them</option>
    </select>



    <input type="submit" value="Anomalies">
</form>

</body>
</html>