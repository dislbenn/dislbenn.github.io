<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="icon" href="img/favicon.png" type="image/png">
        <title>Services</title>
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
								<li class="nav-item"><a class="nav-link" href="about-us.php">About</a></li> 
								<li class="nav-item active"><a class="nav-link" href="services.php">Services</a>
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
						<h2>Services</h2>
						<div class="page_link">
							<a href="index.html">HOME</a>
							<a href="services.html">SERVICE</a>
						</div>
					</div>
				</div>
            </div>
        </section>
        <!--================End Home Banner Area =================-->
        
        <!--================Work Area =================-->
        <section class="work_area p_120">
        	<div class="container">
        		<div class="main_title">
					<h2>How It work for you</h2>
				</div>
				<p style="float: left; margin-left: 4%; margin-top: 6%; font-size: 1.26vw; width: 40%;">This open source system web-crawler mines the data from
					a website and stores the retreived data into various csv files for the user.<br><br>
				<strong>
					The recordings below, demonstrate how the software extracts data from Walmart,
					and displays the product's: name, price, rating, link, and reviews. 
				</strong>
				</p>
				<img src="images/data-mining.png" style="width: 48%; float: right; margin-bottom: 10%;">
				<table style="width: 100%; margin-bottom: 2%; margin-top: 10%; margin-left: -4%;">
					<tr>	
						<td align="center" style="width:25%;">
							<img class="img-fluid" src="images/crawler.png" alt="" style="margin-bottom: 10%; width:50%;">
						</td>
						<td>
							<h3>Web-Crawler</h3>
							<p style="font-size: 1.5vw;">
								Designed on the key components of data mining, the <u>web-crawler</u> can extract data,
								log extraction success/failure, compress data/files, file management, and database management.
							</p>
						</td>
					</tr>
				</table>
				<table style="width: 100%; margin-bottom: 2%; margin-left: 4%;">
					<tr>	
						<td>
							<h3>Modules</h3>
							<p style="font-size: 1.5vw;">
								<u>Product Extraction</u> when tested locally or running remotely, will deliver your application
								information extracted from the targeted website.<br /><br />

								<u>CSV Database</u> when tested locally, the web-crawler stores the retreived data into various csv files,
								and store the application data within an SQL database.
							</p>
						</td>
						<td align="center" style="width:25%;">
							<img class="img-fluid" src="images/module.png" alt="" style="margin-bottom: 10%; width:50%;">
						</td>
					</tr>
				</table>
				<table style="width: 100%; margin-bottom: 2%; margin-left: -4%;">
					<tr>	
						<td align="center" style="width:25%;">
							<img class="img-fluid" src="images/csv.png" alt="" style="margin-bottom: 10%; width:50%;">
						</td>
						<td>
							<h3>CSV</h3>
							<p style="font-size: 1.5vw;">
								CSV files are created based upon the data extraction inititalized during the web-crawler testing.
								Copies of the CSV is constructed for the user, company, and developer view.
							</p>
						</td>
					</tr>
				</table>
				<table style="width: 100%; margin-bottom: 2%; margin-left: 4%;">
					<tr>	
						<td>
							<h3>Logs</h3>
							<p style="font-size: 1.5vw;">
								Log files are generated incrementally during the data extraction inititalized when testing. 
								Upon future release, data logs will be stored in a database for future analysis.
							</p>
						</td>
						<td align="center" style="width:25%;">
							<img class="img-fluid" src="images/log.png" alt="" style="margin-bottom: 10%; width:50%;">
						</td>
					</tr>
				</table>
				<table style="width: 100%">
					<tr>
						<td>
							<video width="100%" height="400" controls style="padding: 10px">
								<source src="videos/bas_web_crawler_tutorial.mov">
							</video>
							<figcaption align="center" style="font-size: 1.5vw;"><u>Basic web-crawler tutorial, for (developers)</u></figcaption>
						</td>
						<td>
							<video width="100%" height="400" controls style="padding: 10px">
								<source src="videos/bas_web_crawler_tutorial.mov">
							</video>
							<figcaption align="center" style="font-size: 1.5vw;"><u>Basic web-crawler tutorial, for (customers)</u></figcaption>
						</td>
					</tr>
				</table>
        	</div>
        </section>
        <!--================End Work Area =================-->
       
        <!--================Footer Area =================-->
        <footer class="footer_area p_120">
        	<div class="container">
        		<div class="row footer_inner">
        			<div class="col-lg-5 col-sm-6">
        				<aside class="f_widget ab_widget">
        					<div class="f_title">
        						<h3>About Me</h3>
        					</div>
        					<p>
								My name is Disaiah Bennett, and I am a senior undergraduate student at ECSU. Currently, I am studying in the field of computer science, 
								with a minor in mathematics. After graduation, I plan on starting a career in software development and then returning to acquire my masters.
							</p>
        					<p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        				</aside>
        			</div>
        			<div class="col-lg-5 col-sm-6">
        				<aside class="f_widget news_widget">
        					<div class="f_title">
        						<h3>Newsletter</h3>
        					</div>
        					<p>Stay updated with our latest trends</p>
        					<div id="mc_embed_signup">
                                <form target="_blank" action="https://spondonit.us12.list-manage.com/subscribe/post?u=1462626880ade1ac87bd9c93a&amp;id=92a4423d01" method="get" class="subscribe_form relative">
                                	<div class="input-group d-flex flex-row">
                                        <input name="EMAIL" placeholder="Enter email address" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Email Address '" required="" type="email">
                                        <button class="btn sub-btn"><span class="lnr lnr-arrow-right"></span></button>		
                                    </div>				
                                    <div class="mt-10 info"></div>
                                </form>
                            </div>
        				</aside>
        			</div>
        			<div class="col-lg-2">
        				<aside class="f_widget social_widget">
        					<div class="f_title">
        						<h3>Follow Me</h3>
        					</div>
        					<p>Let us be social</p>
        					<ul class="list">
        						<li><a href="https://www.facebook.com/Disaiah.Bennett" target="_blanks"><i class="fa fa-facebook"></i></a></li>
        						<li><a href="#"><i class="fa fa-twitter"></i></a></li>
        						<li><a href="https://www.instagram.com/disaiah.bennett/" target="_blanks"><i class="fa fa-instagram"></i></a></li>
        						<li><a href="https://www.linkedin.com/in/disaiah-bennett-062153164/" target="_blanks"><i class="fa fa-linkedin"></i></a></li>
        					</ul>
        				</aside>
        			</div>
        		</div>
        	</div>
        </footer>
        <!--================End Footer Area =================-->
        
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