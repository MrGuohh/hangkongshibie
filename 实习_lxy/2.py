{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
        * {
            margin: 0;
            padding: 0;
        }
        html {
            height: 110%;
        }
        body {
            height: 110%;
        }
        .container {
            height: 100%;
            background-image: linear-gradient(to right, #999999, #5d86af);
        }
        .login-wrapper {
            background-color: bisque;
            width: 550px;
            height: 350px;
            border-radius: 15px;
            padding: 0 50px;
            position: relative;
            left: 50%;
            top: 50%;
            transform: translate(-50%,-50%);
        }
        .header1 {
            font-size: 35px;
            font-weight: bold;
            text-align: center;
            line-height: 125px;
        }
        .header2 {
            font-size: 15px;
            font-weight: bold;
            left:40%;
            line-height: 30px;
            display:inline;
        }
        .header3 {
            font-size: 15px;
            font-weight: bold;
            left:43%;
            line-height: 30px;
            display:inline;
        }
        .input-item {
            display: block;
            width: 100%;
            margin-bottom: 20px;
            border: 0;
            padding: 10px;
            border-bottom: 1px solid rgb(128,125,125);
            font-size: 15px;
            outline: none;
        }
        .input-item::placeholder {
            text-transform: uppercase;
        }
        .btn1 {
            text-align: center;
            padding: 10px;
            width: 15%;
            height:30%;
            margin-top: 30px;
            position:absolute;
            left:50px;
            display:inline;
            background-image: linear-gradient(to right,#a6c1ee, #b5e2b5);
            color: #fff;
        }
        .btn2 {
            text-align: center;
            padding: 10px;
            width: 15%;
            height:30%;
            margin-top: 30px;
            position:absolute;
            left:200px;
            display:inline;
            background-image: linear-gradient(to right,#a6c1ee, #b5e2b5);
            color: #fff;
        }
        .btn3 {
            text-align: center;
            padding: 10px;
            width: 12%;
            height:10%;
            margin-top: 60px;
            position:absolute;
            left:450px;
            display:inline;
            background-image: linear-gradient(to right,#a6c1ee, #b5e2b5);
            color: #fff;
        }
        .btn4 {
            text-align: center;
            padding: 10px;
            width: 12%;
            height:10%;
            margin-top: 60px;
            position:absolute;
            left:550px;
            display:inline;
            background-image: linear-gradient(to right,#a6c1ee, #b5e2b5);
            color: #fff;
        }
        a {
            text-decoration-line: none;
            color: #abc1ee;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-wrapper">
            <div class="header1">欢迎购票</div>
            <div class="form-wrapper">
                <div class="header2">
                    起飞地:
                    <select name="" class="">
                        <option> - - 请选择地点 - - </option>
                        <option>湖北</option>
                        <option>湖南</option>
                        <option>河北</option>
                        <option>河南</option>
                        <option>东北</option>
                    </select>
                    <!-- <img src="../web/images/logo.jpg" width="100" height="75" style="margin-top: 10%;margin-left: 10%;"/> -->
<!-- {% static '/images/registerimg.png' %} -->
                    <br />
                    目的地:
                    <select name="" class="">
                        <option> - - 请选择地点 - - </option>
                        <option>湖北</option>
                        <option>湖南</option>
                        <option>河北</option>
                        <option>河南</option>
                        <option>东北</option>
                    </select>
                    <br />
                    <br />
                    <br />
                    <form>
                        <button onclick="ses()" style="border: none"  left="100px" class="btn3">购买</button>
                    </form>
                    <form action="{% url 'web_dologin' %}" method="post">
                        {% csrf_token %}
                        <button type="submit" style="border: none"  left="100px" class="btn4">退出</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>
<script>
    function ses(){
        alert('购买成功！');
    }
</script>
</html>