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
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["image"]["name"]);
    if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
        $file_size = filesize($target_file);
        list($width, $height) = getimagesize($target_file);
        list($avg_r, $avg_g, $avg_b) = getAverageColor($target_file);
        // Règle simple : si avg_r < 100 ET file_size > 100ko => pleine
        $auto_annotation = ($avg_r < 100 && $file_size > 100*1024) ? 'full' : $_POST['annotation'];
        $stmt = $pdo->prepare("INSERT INTO images (filename, annotation, file_size, width, height, avg_r, avg_g, avg_b) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->execute([
            basename($_FILES["image"]["name"]),
            $auto_annotation,
            $file_size,
            $width,
            $height,
            $avg_r,
            $avg_g,
            $avg_b
        ]);
        header("Location: images.php");
        exit();
    } else {
        echo "Erreur lors de l'upload.";
    }
}
?>
<!-- Formulaire HTML -->
<?php include 'menu.php'; ?>
<h2>Uploader une image de poubelle</h2>
<form method="post" enctype="multipart/form-data">
    <input type="file" name="image" required>
    <select name="annotation">
        <option value="full">Pleine</option>
        <option value="empty">Vide</option>
    </select>
    <button type="submit">Uploader</button>
</form> 