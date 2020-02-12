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

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\vizualiseOil.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }
        String csvFile = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Crude_Oil_Prices_Brent.csv";
        BufferedReader br = null;
        String line = "";
        String csvSplitBy = ",";

        int count = 0;


        try {

            out.print("<textarea rows="+30+" cols="+35+">");
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] values = line.split(csvSplitBy);

                out.print( " [Date=" + values[0] + " , Value=" + values[1] + "]");

                count += 1;
            }

            out.print("</textarea >");



//            out.print("<p id=\"demo\"></p>");

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }



    }else if (data.equals("unrate")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\vizualiseUnempl.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }
        String csvFile = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Unemployment_Rate.csv";
        BufferedReader br = null;
        String line = "";
        String csvSplitBy = ",";

        int count = 0;


        try {

            out.print("<textarea rows="+30+" cols="+35+">");
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] values = line.split(csvSplitBy);

                out.print( " [Date=" + values[0] + " , Value=" + values[1] + "]");

                count += 1;
            }

            out.print("</textarea >");



//            out.print("<p id=\"demo\"></p>");

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }else if (data.equals("sales")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\vizualise.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

        String csvFile = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv";
        BufferedReader br = null;
        String line = "";
        String csvSplitBy = ",";

        int count = 0;


        try {

            out.print("<textarea rows="+30+" cols="+35+">");
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] values = line.split(csvSplitBy);

                out.print( " [Date=" + values[0] + " , Value=" + values[1] + "]");

                count += 1;
            }

            out.print("</textarea >");



//            out.print("<p id=\"demo\"></p>");

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }


%>

</form>
<form align = "center" action="save.jsp">
    <br/>Write anomalous Values separated with comma: <br/>
    <textarea align="center" name="text"  rows=5 cols=50></textarea>
    <br/>
    <input align="center" type="submit">

</form>

</body>
</html>