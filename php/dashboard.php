<?php
include 'db.php';
$total = $pdo->query("SELECT COUNT(*) FROM images")->fetchColumn();
$pleines = $pdo->query("SELECT COUNT(*) FROM images WHERE annotation='full'")->fetchColumn();
$vides = $pdo->query("SELECT COUNT(*) FROM images WHERE annotation='empty'")->fetchColumn();
$stats = $pdo->query("SELECT AVG(file_size) as avg_size, AVG(width) as avg_width, AVG(height) as avg_height, AVG(avg_r) as avg_r, AVG(avg_g) as avg_g, AVG(avg_b) as avg_b FROM images")->fetch(PDO::FETCH_ASSOC);
?>
<?php include 'menu.php'; ?>
<h2>Statistiques</h2>
<ul>
    <li>Total images : <?= $total ?></li>
    <li>Poubelles pleines : <?= $pleines ?></li>
    <li>Poubelles vides : <?= $vides ?></li>
    <li>Taille moyenne : <?= round($stats['avg_size']/1024,1) ?> ko</li>
    <li>Dimensions moyennes : <?= round($stats['avg_width']) . 'x' . round($stats['avg_height']) ?></li>
    <li>Couleur moyenne globale : <span style="background:rgb(<?= round($stats['avg_r']) ?>,<?= round($stats['avg_g']) ?>,<?= round($stats['avg_b']) ?>);color:#fff;padding:2px 8px;">
        <?= round($stats['avg_r']) ?>,<?= round($stats['avg_g']) ?>,<?= round($stats['avg_b']) ?>
    </span></li>
</ul> 