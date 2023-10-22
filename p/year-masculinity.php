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
            <img src="../assets/img/profile-img.jpg" alt="Profile" class="rounded-circle">
            <span class="d-none d-md-block dropdown-toggle ps-2">K. Anderson</span>
          </a><!-- End Profile Iamge Icon -->

          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow profile">
            <li class="dropdown-header">
              <h6>Kevin Anderson</h6>
              <span>Principle</span>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li onclick="getdata('1', 'y');">
              <a class="dropdown-item d-flex align-items-center" href="#">
                <i class="bi bi-person"></i>
                <span>Survey 01</span>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li onclick="getdata('2', 'y');">
              <a class="dropdown-item d-flex align-items-center" href="#">
                <i class="bi bi-person"></i>
                <span>Survey 02</span>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li>
              <a class="dropdown-item d-flex align-items-center" href="#">
                <i class="bi bi-person"></i>
                <span>Upload XLSX</span>
              </a>
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
        <a class="nav-link" data-bs-target="#charts-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-bar-chart"></i><span>Years</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="charts-nav" class="nav-content collapse show" data-bs-parent="#sidebar-nav">
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
            <a href="year-masculinity.php" class="active">
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
      </li>
      <li class="nav-item">
        <a class="nav-link collapsed" href="clubs.php">
          <i class="bi bi-gem"></i>
          <span>Clubs</span>
        </a>
      </li>

    </ul>

  </aside><!-- End Sidebar-->

  <main id="main" class="main">

    <div class="pagetitle">
      <h1>Masculinity Analysis</h1>
      <nav>
        <ol class="breadcrumb">
          <li class="breadcrumb-item" id="survey_num">Survey 01 Analysis</li>
        </ol>
      </nav>
    </div><!-- End Page Title -->
      <br>

<section class="section">
  <div class="row">
    <div class="col-lg-12">

      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Average Masculinity Score</h5>
          <!-- Vertical Bar Chart -->
          <div id="masculinity" style="min-height: 500px;" class="echart"></div>
          <!-- End Vertical Bar Chart -->
        </div>
      </div>

    </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="row">
    <div class="col-lg-6">

      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Masculinity and Language</h5>
          <!-- Vertical Bar Chart -->
          <div id="language" style="min-height: 500px;" class="echart"></div>
          <!-- End Vertical Bar Chart -->
        </div>
      </div>

    </div>

    <div class="col-lg-6">

      <div class="card">
        <div class="card-body"><br>
          <!-- Table with hoverable rows -->
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Years</th>
                <th scope="col">English</th>
                <th scope="col">Non-English</th>
              </tr>
            </thead>
            <tbody id="language_tbl">
            </tbody>
          </table>
          <!-- End Table with hoverable rows -->
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
  <script src="masculinity.js"></script>
  <script>getdata("1", "y");</script>

</body>

</html>