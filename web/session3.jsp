<%--
  Created by IntelliJ IDEA.
  User: petro
  Date: 15/1/2020
  Time: 19:51
  To change this template use File | Settings | File Templates.
--%>
<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.InputStreamReader" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Title</title>
</head>
<body>
<%


    String item = request.getParameter("item");

    session.setAttribute("item", item);      //set attribute in session



    if (item.equals("svm")){


        try{
            String str = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\petro\\IdeaProjects\\Thesisbp\\svmAnom.py");
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((str = input.readLine())!= null){
                System.out.println(str);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }else if (item.equals("islforest")){

        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\petro\\IdeaProjects\\Thesisbp\\isolationForestAnom.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }
    }else if (item.equals("sax")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\petro\\IdeaProjects\\Thesisbp\\saxAnom.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }else if (item.equals("all")){

        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\petro\\IdeaProjects\\Thesisbp\\MyThesis.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }

%>
<h2>Thanks for using my app! :)</h2>

</body>
</html>
