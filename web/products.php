<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="icon" href="img/favicon.png" type="image/png">
        <title><?php echo str_replace("_", " ", $_GET["category"]);?> Products</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="css/bootstrap.css">
        <link rel="stylesheet" href="vendors/linericon/style.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <link rel="stylesheet" href="vendors/owl-carousel/owl.carousel.min.css">
        <link rel="stylesheet" href="vendors/lightbox/simpleLightbox.css">
        <link rel="stylesheet" href="vendors/nice-select/css/nice-select.css">
        <link rel="stylesheet" href="vendors/animate-css/animate.css">
        <!-- main css -->
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/responsive.css">
    </head>
    <body>
        
        <!--================Header Menu Area =================-->
        <header class="header_area">
            <div class="main_menu">
            	<nav class="navbar navbar-expand-lg navbar-light">
					<div class="container box_1620">
						<!-- Brand and toggle get grouped for better mobile display -->
						<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<!-- Collect the nav links, forms, and other content for toggling -->
						<div class="collapse navbar-collapse offset" id="navbarSupportedContent">
							<ul class="nav navbar-nav menu_nav justify-content-center">
								<li class="nav-item"><a class="nav-link" href="index.html">Home</a></li> 
								<li class="nav-item active"><a class="nav-link" href="about-us.php">About</a></li> 
								<li class="nav-item"><a class="nav-link" href="services.php">Services</a>
								<li class="nav-item"><a class="nav-link" href="contact.php">Contact</a></li>
                                <li class="nav-item"><a class="nav-link" href="documentation.html">Documentation</a></li>
								<!--li class="nav-item"><a class="nav-link" href="doc/build/html/genindex.html" target="_blanks">Documentation</a></li-->
								<li class="nav-item"><a class="nav-link" href="../index.html">Creator</a></li>
								<li class="nav-item"><a class="nav-link" href="#">v0.1</a></li>
							</ul>
						</div> 
					</div>
            	</nav>
            </div>
        </header>
        <!--================Header Menu Area =================-->
        
        <!--================Home Banner Area =================-->
        <section class="banner_area">
            <div class="banner_inner d-flex align-items-center">
            	<div class="overlay bg-parallax" data-stellar-ratio="0.9" data-stellar-vertical-offset="0" data-background=""></div>
				<div class="container">
					<div class="banner_content text-center">
						<h2><?php echo str_replace("_", " ", $_GET["category"]);?></h2>
						<div class="page_link">
							<a href="index.html">Home</a>
                            <a href="about-us.php"><?php echo str_replace("_", " ", $_GET["category"]);?> Products</a>
                        </div>
                        <br>
                        <h5 style='color:white;'>Click the product's rating score to view the reviews about that product.</h5> 
					</div>
				</div>
            </div>
        </section>
        <!--================End Home Banner Area =================-->
		<?php
			$servername = 'localhost';
			$username = 'root';
			$password = '';
            $dbname = "Web-Crawler";
            
            $category = str_replace('_', '', $_GET["category"]);
            $subcategory = explode('_', $_GET["category"]);

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			}

            $sql = "SELECT * FROM `$category` ORDER BY `Rating` DESC";
			$result = $conn->query($sql);
		?>
        <!--================Made Life Area =================-->
		<span style="border: 3 solid black">
		<?php 
			$count = 0;
			echo "<table width=100% border>\n";
			echo "<tr align='center'><th><u>Product Name</u><th><u>Price</u></th><th><u>Description</u></th><th><u>Rating</u></th></tr>";
			while($row = $result->fetch_assoc()) {
                echo "<tr style='color:black'><td width=12% align='center'><a href='".$row["Link"]."'>".$row["Product_Name"]."</a></td><td width=5% align='center'>".$row["Price"]."</td><td>".$row["About"]."</td><td align='center' width='5%'><a href='review.php?cat=$category&rev=$row[Product_Name]'>".$row["Rating"]."</a></td></tr>";
			}	
		?>
		</span>
        <!--================End Made Life Area =================-->    
        
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="js/jquery-3.2.1.min.js"></script>
        <script src="js/popper.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/stellar.js"></script>
        <script src="vendors/lightbox/simpleLightbox.min.js"></script>
        <script src="vendors/nice-select/js/jquery.nice-select.min.js"></script>
        <script src="vendors/isotope/imagesloaded.pkgd.min.js"></script>
        <script src="vendors/isotope/isotope-min.js"></script>
        <script src="vendors/owl-carousel/owl.carousel.min.js"></script>
        <script src="js/jquery.ajaxchimp.min.js"></script>
        <script src="js/mail-script.js"></script>
        <script src="vendors/counter-up/jquery.waypoints.min.js"></script>
        <script src="vendors/counter-up/jquery.counterup.min.js"></script>
        <script src="js/theme.js"></script>
    </body>
</html>