<?php
include 'db.php';
function getAverageColor($file) {
    $img = imagecreatefromstring(file_get_contents($file));
    $width = imagesx($img);
    $height = imagesy($img);
    $r = $g = $b = 0;
    $total = 0;
    for ($x = 0; $x < $width; $x += max(1, intval($width/50))) {
        for ($y = 0; $y < $height; $y += max(1, intval($height/50))) {
            $rgb = imagecolorat($img, $x, $y);
            $r += ($rgb >> 16) & 0xFF;
            $g += ($rgb >> 8) & 0xFF;
            $b += $rgb & 0xFF;
            $total++;
        }
    }
    imagedestroy($img);
    return [round($r/$total), round($g/$total), round($b/$total)];
}
function import_dir($dir, $annotation) {
    global $pdo;
    $files = glob($dir.'/*.{jpg,jpeg,png}', GLOB_BRACE);
    foreach ($files as $file) {
        $file_size = filesize($file);
        list($width, $height) = getimagesize($file);
        list($avg_r, $avg_g, $avg_b) = getAverageColor($file);
        $stmt = $pdo->prepare("INSERT INTO images (filename, annotation, file_size, width, height, avg_r, avg_g, avg_b) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->execute([
            basename($file),
            $annotation,
            $file_size,
            $width,
            $height,
            $avg_r,
            $avg_g,
            $avg_b
        ]);
    }
}
import_dir('../Data/train/with_label/clean', 'empty');
import_dir('../Data/train/with_label/dirty', 'full');
echo "Import terminé !"; 