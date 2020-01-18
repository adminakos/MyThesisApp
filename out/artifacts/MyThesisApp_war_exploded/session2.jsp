<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.*" %>
<%@ page import="java.lang.*" %>
<%@ page import="java.io.OutputStream" %>
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
    String item =(String) session.getAttribute("item");




    if (item.equals("svm")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\saveSVMdataAnom.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }


        String filename = "C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\svmanomalies.csv";
        response.setContentType("application/octet-stream");
        String disHeader = "Attachment; Filename=\"svmanomalies.csv\"";
        response.setHeader("Content-Disposition", disHeader);
        File fileToDownload = new File(filename);

        InputStream in = null;
        OutputStream outs = response.getOutputStream();

        try {
            in = new BufferedInputStream
                    (new FileInputStream(fileToDownload));
            int ch;
            while ((ch = in.read()) != -1) {
                outs.write((char) ch);
            }
        }
        finally {
            if (in != null) in.close(); // very important
        }

        outs.flush();
        outs.close();
        in.close();

    }else if (item.equals("islforest")){


        try{
            String s = null;

            Process p=Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\saveISOLdataAnom.py");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((s = in.readLine())!= null){
                System.out.println(s);

            }
        }catch(Exception e) {
            e.printStackTrace();
        }


        String filename = "C:\\Users\\Βασίλης\\IdeaProjects\\thesis_python_scripts\\isolationanomalies.csv";
        response.setContentType("application/octet-stream");
        String disHeader = "Attachment; Filename=\"isolationanomalies.csv\"";
        response.setHeader("Content-Disposition", disHeader);
        File fileToDownload = new File(filename);

        InputStream in = null;
        OutputStream outs = response.getOutputStream();

        try {
            in = new BufferedInputStream
                    (new FileInputStream(fileToDownload));
            int ch;
            while ((ch = in.read()) != -1) {
                outs.write((char) ch);
            }
        }
        finally {
            if (in != null) in.close(); // very important
        }

        outs.flush();
        outs.close();
        in.close();
    }


%>




</body>
</html>