<?php 
  require "localhost.php"; // import file koneksi
  include "header.php";
?>

</nav>
<tbody>
<table class="table table-bordered" style="text-align: left;">
  <thead>
    <th>No</th>
    <th>Authors Name</th>
     
  </thead>

</tbody>

  <?php 

  $sql = "SELECT * FROM (nama_buku inner join pengarang on pengarang.Nomer = Nama_buku.Nomer)"; 
  $result = mysqli_query($mysql, $sql);

  while ($data = mysqli_fetch_array($result)) {

   ?>
  
    <tr>
  <td><?php echo $data['Nomer']; ?></td>
  <td><?php echo $data['pengarang']; ?></td>
   
  </tr>

  <?php } ?>
  </table>

  </body>
  </html>
  <?php include "footer.php"; ?>