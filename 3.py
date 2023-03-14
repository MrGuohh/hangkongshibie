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
            width: 350px;
            height: 550px;
            border-radius: 15px;
            padding: 0 50px;
            position: relative;
            left: 80%;
            top: 50%;
            transform: translate(-50%,-50%);
        }
        .header {
            font-size: 35px;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
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
            width: 20%;
            margin-top: 30px;
            position:absolute;
            left:325px;
            background-image: linear-gradient(to right,#a6c1ee, #ce6d73);
            color: #fff;
        }
        .btn2 {
            text-align: center;
            padding: 10px;
            width: 20%;
            margin-top: 10px;
            position:absolute;
            left:35px;
            background-image: linear-gradient(to right,#a6c1ee, #ce6d73);
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
            <div class="header">欢迎登录购票系统~</div>
            <div class="form-wrapper">
                <input type="text" name="telenumber" placeholder="输入手机号" class="input-item">
                <input type="password" name="password" placeholder="输入密码（默认身份证后六位）" class="input-item">
                <form action="{% url 'web_dologin' %}" method="post">
                    {% csrf_token %}
                    <button type="submit" style="border: none"  left="100px" class="btn1">登录</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>