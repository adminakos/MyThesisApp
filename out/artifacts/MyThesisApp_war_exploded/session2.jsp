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
    String data =(String) session.getAttribute("data");



    if (item.equals("svm") ){

        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveSVMoil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "svmanomaliesoil.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"svmanomaliesoil.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }else if(data.equals("unrate")){

            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveSVMunempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "svmanomaliesunempl.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"svmanomaliesunempl.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }else if (data.equals("sales")){

            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveSVMdataAnom.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "svmanomaliessales.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"svmanomaliessales.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }

    }else if (item.equals("islforest")){

        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveISOLoil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "isolationanomaliesoil.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"isolationanomaliesoil.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }else if(data.equals("unrate")){

            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveISOLunempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "isolationanomaliesunemp.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"isolationanomaliesunemp.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }else if (data.equals("sales")){

            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saveISOLdataAnom.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }


            String filename = "isolationanomaliessales.csv";
            response.setContentType("application/octet-stream");
            String disHeader = "Attachment; Filename=\"isolationanomaliessales.csv\"";
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
            } finally {
                if (in != null) in.close(); // very important
            }

            outs.flush();
            outs.close();
            in.close();
        }
    }


%>




</body>
</html>