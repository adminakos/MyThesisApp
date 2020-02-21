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
    String data =(String) session.getAttribute("data");


    if (item.equals("svm")){

        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\svmAnomOil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }else if(data.equals("unrate")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\svmAnomUnempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }else if(data.equals("sales")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\svmAnom.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }

    }else if (item.equals("islforest")){
        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\isolationForestAnomOil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }else if(data.equals("unrate")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\isolationForestAnomUnempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }else if(data.equals("sales")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\isolationForestAnom.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }
    }else if (item.equals("sax")){

        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saxThesisOil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }else if(data.equals("unrate")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\saxThesisUnempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }else if(data.equals("sales")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\Thesis.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }



    }else if (item.equals("kmeans")){
        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\kmeans2Oil.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }

            } catch (Exception e) {
                e.printStackTrace();
            }
        }else if(data.equals("unrate")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\kmeans2unempl.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }else if(data.equals("sales")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\kmeans2.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }
    }else if (item.equals("zscore")){

        if(data.equals("oil")) {
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\oilZ_score.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }else if(data.equals("unrate")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\z_score.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }else if(data.equals("sales")){
            try {
                String s = null;

                Process p = Runtime.getRuntime().exec("python C:\\Users\\Βασίλης\\IdeaProjects\\MyThesisApp\\TVZ_score.py");
                BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = in.readLine()) != null) {
                    System.out.println(s);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }

        }

    }

%>
<h2>Thanks for using my app! :)</h2>
<p>Please feel free to download the data set with the outliers you just saw.</p>
<form action="session2.jsp">
    <input type="submit" value="Download">

</form>

<form action="compare.jsp">
    <input type="submit" value="Compare Algorithms">

</form>

</body>
</html>
