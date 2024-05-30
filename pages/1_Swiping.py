import streamlit as st
import streamlit.components.v1 as components

st.title("Swiper Cards with Streamlit")

# Define the HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Swiper Cards Example</title>
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <style>
        .swiper-container {
            width: 100%;
            max-width: 600px;
            height: 400px;
            margin: 0 auto;
        }
        .swiper-slide {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 22px;
            color: #fff;
            background-color: #007aff;
        }
        .swiper-slide img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <img src="images/image1.jpg" alt="Image 1">
            </div>
            <div class="swiper-slide">
                <img src="images/image2.jpg" alt="Image 2">
            </div>
            <div class="swiper-slide">
                <img src="images/image3.jpg" alt="Image 3">
            </div>
        </div>
        <!-- Add Pagination -->
        <div class="swiper-pagination"></div>
        <!-- Add Navigation -->
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>
    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper('.swiper-container', {
            pagination: {
                el: '.swiper-pagination',
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    </script>
</body>
</html>
"""

# Embed the HTML and JavaScript code in Streamlit
components.html(html_code, height=600)
