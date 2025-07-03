<?php
$host = "localhost";
$dbname = "NOM_DE_TA_BDD"; // À remplacer par le nom de ta base
$user = "UTILISATEUR_BDD"; // À remplacer par ton utilisateur
$pass = "MOT_DE_PASSE_BDD"; // À remplacer par ton mot de passe
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}
// Création de la table si elle n'existe pas
$pdo->exec("CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    annotation VARCHAR(10),
    file_size INT,
    width INT,
    height INT,
    avg_r INT,
    avg_g INT,
    avg_b INT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)");
?> 