<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>SNA - Team 05</title>

  <!-- Favicons -->
  <link href="../assets/img/favicon.png" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.gstatic.com" rel="preconnect">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="../assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="../assets/vendor/quill/quill.snow.css" rel="stylesheet">
  <link href="../assets/vendor/quill/quill.bubble.css" rel="stylesheet">
  <link href="../assets/vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="../assets/vendor/simple-datatables/style.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="../assets/css/style.css" rel="stylesheet">

</head>

<body>

  <!-- ======= Header ======= -->
  <header id="header" class="header fixed-top d-flex align-items-center">

    <div class="d-flex align-items-center justify-content-between">
      <a href="index.php" class="logo d-flex align-items-center">
        <img src="../assets/img/logo.png" alt="">
        <span class="d-none d-lg-block">SNA</span>
      </a>
      <i class="bi bi-list toggle-sidebar-btn"></i>
    </div><!-- End Logo -->


    <nav class="header-nav ms-auto">
      <ul class="d-flex align-items-center">

        <li class="nav-item dropdown pe-3">

          <a class="nav-link nav-profile d-flex align-items-center pe-0" href="#" data-bs-toggle="dropdown">
            <img src="../assets/img/outsider.jpg" alt="Profile" class="rounded-circle">
            <span class="d-none d-md-block dropdown-toggle ps-2">Luke</span>
          </a><!-- End Profile Iamge Icon -->

          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow profile">
            <li class="dropdown-header">
              <h6>Luke Anderson</h6>
              <span>Guest</span>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li>
              <hr class="dropdown-divider">
            </li>

            <li>
              <a class="dropdown-item d-flex align-items-center" href="../">
                <i class="bi bi-box-arrow-right"></i>
                <span>Sign Out</span>
              </a>
            </li>

          </ul><!-- End Profile Dropdown Items -->
        </li><!-- End Profile Nav -->

      </ul>
    </nav><!-- End Icons Navigation -->

  </header><!-- End Header -->

  <!-- ======= Sidebar ======= -->
  <aside id="sidebar" class="sidebar">

    <ul class="sidebar-nav" id="sidebar-nav">

      <li class="nav-item">
        <a class="nav-link collapsed" href="index.php">
          <i class="bi bi-grid"></i>
          <span>Dashboard</span>
        </a>

      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#charts-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-bar-chart"></i><span>Years</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="charts-nav" class="nav-content collapse" data-bs-parent="#sidebar-nav">
          <li>
            <a href="year-academic.php">
              <i class="bi bi-circle"></i><span>Academic Performance</span>
            </a>
          </li>
          <li>
            <a href="year-k6.php">
              <i class="bi bi-circle"></i><span>K6</span>
            </a>
          </li>
          <li>
            <a href="year-manbox.php">
              <i class="bi bi-circle"></i><span>Manbox</span>
            </a>
          </li>
          <li>
            <a href="year-masculinity.php">
              <i class="bi bi-circle"></i><span>Masculinity</span>
            </a>
          </li>
          <li>
            <a href="year-engagement.php">
              <i class="bi bi-circle"></i><span>School Engagement</span>
            </a>
          </li>
          <li>
            <a href="year-growthmindset.php">
              <i class="bi bi-circle"></i><span>Growth Mindset</span>
            </a>
          </li>
        </ul>
      </li><!-- End Charts Nav -->

      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#tables-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-layout-text-window-reverse"></i><span>Houses</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="tables-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="house-academic.php">
              <i class="bi bi-circle"></i><span>Academic Performance</span>
            </a>
          </li>
          <li>
            <a href="house-k6.php">
              <i class="bi bi-circle"></i><span>K6</span>
            </a>
          </li>
          <li>
            <a href="house-manbox.php">
              <i class="bi bi-circle"></i><span>Manbox</span>
            </a>
          </li>
          <li>
            <a href="house-masculinity.php">
              <i class="bi bi-circle"></i><span>Masculinity</span>
            </a>
          </li>
          <li>
            <a href="house-engagement.php">
              <i class="bi bi-circle"></i><span>School Engagement</span>
            </a>
          </li>
          <li>
            <a href="house-growthmindset.php">
              <i class="bi bi-circle"></i><span>Growth Mindset</span>
            </a>
          </li>
        </ul>
      </li><!-- End Tables Nav -->

      <li class="nav-item">
        <a class="nav-link" href="clubs.php">
          <i class="bi bi-gem"></i>
          <span>Clubs</span>
        </a>
      </li>

    </ul>

  </aside><!-- End Sidebar-->

  <main id="main" class="main">

    <div class="pagetitle">
      <h1></h1>
      <nav>
      </nav>
    </div><!-- End Page Title -->
    <br>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="row">
                <div class="col-lg-3">
                  <h5 class="card-title">Select the Category</h5>
                  <select class="form-select" aria-label="Select a category" id="cat">
                    <option selected disabled>Select a category</option>
                    <option value="net_0_Friends">net_0_Friends</option>
                    <option value="net_1_Influential">net_1_Influential</option>
                    <option value="net_2_Feedback">net_2_Feedback</option>
                    <option value="net_3_MoreTime">net_3_MoreTime</option>
                    <option value="net_4_Advice">net_4_Advice</option>
                    <option value="net_5_Disrespect">net_5_Disrespect</option>
                  </select>
                </div>
                <!--
                <div class="col-lg-3">
                  <h5 class="card-title">Select Club</h5>
                  <select class="form-select" aria-label="Select a club" id="survey">
                    <option selected disabled>Select a club</option>
                    <option value="Photography Club">Photography Club</option>
                    <option value="Gardening Club">Gardening Club</option>
                    <option value="Diversity and Inclusion Club">Diversity and Inclusion Club</option>
                    <option value="Yoga Club">Yoga Club</option>
                    <option value="Technology Club">Technology Club</option>
                    <option value="Student Council">Student Council</option>
                    <option value="Chess Club">Chess Club</option>
                    <option value="Fitness/Health Club">Fitness/Health Club</option>
                    <option value="Chess Team">Chess Team</option>
                    <option value="Environmental Club">Environmental Club</option>
                    <option value="Science Club">Science Club</option>
                    <option value="National Honor Society">National Honor Society</option>
                    <option value="Astronomy Club">Astronomy Club</option>
                    <option value="Culinary Club">Culinary Club</option>
                    <option value="Anime Club">Anime Club</option>
                    <option value="Film Club">Film Club</option>
                    <option value="Math Club">Math Club</option>
                    <option value="Psychology Club">Psychology Club</option>
                    <option value="Community Service Club">Community Service Club</option>
                    <option value="Debate Team">Debate Team</option>
                    <option value="Creative Writing Club">Creative Writing Club</option>
                    <option value="Debate Club">Debate Club</option>
                    <option value="History Club">History Club</option>
                    <option value="Dance Club">Dance Club</option>
                    <option value="Drama Club">Drama Club</option>
                    <option value="Model United Nations (MUN)">Model United Nations (MUN)</option>
                  </select>
                </div>
-->

                <div class="col-lg-3">
                  <h5 class="card-title">&nbsp;</h5>
                  <button type="button" class="btn btn-outline-primary" onclick="search();">Submit</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title"></h5>
              <div id="clubs_sna" style="min-height: 100vh;" class="echart"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main><!-- End #main -->

  <!-- ======= Footer ======= -->
  <footer id="footer" class="footer">
    <div class="copyright">
      &copy; Copyright <strong><span>NiceAdmin</span></strong>. All Rights Reserved
    </div>
    <div class="credits">
      <!-- All the links in the footer should remain intact. -->
      <!-- You can delete the links only if you purchased the pro version. -->
      <!-- Licensing information: https://bootstrapmade.com/license/ -->
      <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/ -->
      Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
    </div>
  </footer><!-- End Footer -->

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/apexcharts/apexcharts.min.js"></script>
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/chart.js/chart.umd.js"></script>
  <script src="../assets/vendor/echarts/echarts.min.js"></script>
  <script src="../assets/vendor/quill/quill.min.js"></script>
  <script src="../assets/vendor/simple-datatables/simple-datatables.js"></script>
  <script src="../assets/vendor/tinymce/tinymce.min.js"></script>
  <script src="../assets/vendor/php-email-form/validate.js"></script>

  <!-- Template Main JS File -->
  <script src="../assets/js/main.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="clubs.js"></script>

</body>

</html>