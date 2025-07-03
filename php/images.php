<?php
include 'db.php';
$images = $pdo->query("SELECT * FROM images ORDER BY id DESC")->fetchAll(PDO::FETCH_ASSOC);
?>
<?php include 'menu.php'; ?>
<h2>Liste des images uploadées</h2>
<table border="1">
    <tr><th>Image</th><th>Annotation</th><th>Taille (ko)</th><th>Dimensions</th><th>Couleur moyenne</th></tr>
    <?php foreach ($images as $img): ?>
    <tr>
        <td><img src="uploads/<?= htmlspecialchars($img['filename']) ?>" width="100"></td>
        <td><?= htmlspecialchars($img['annotation']) ?></td>
        <td><?= round($img['file_size']/1024,1) ?></td>
        <td><?= $img['width'] . 'x' . $img['height'] ?></td>
        <td style="background:rgb(<?= $img['avg_r'] ?>,<?= $img['avg_g'] ?>,<?= $img['avg_b'] ?>);color:#fff;">
            <?= $img['avg_r'] ?>,<?= $img['avg_g'] ?>,<?= $img['avg_b'] ?>
        </td>
    </tr>
    <?php endforeach; ?>
</table> 