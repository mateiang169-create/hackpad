# Journal de bord - Hackpad (Spotify Music Controller)

## Entrée : Conception complète et fabrication du Hackpad

- **Objectif du projet :** Créer un contrôleur de musique personnalisé (macro-pad) pour Spotify, combinant une interface matérielle avec des touches mécaniques, un encodeur rotatif et un écran OLED.
- **Électronique (KiCad) :** 
  - Dessin du schéma électronique et routage du circuit imprimé (PCB).
  - Intégration du microcontrôleur Seeed XIAO RP2040, des switches mécaniques, de l'encodeur Alps EC11, de l'écran OLED et des diodes de protection.
  - Génération des fichiers de production (Gerber, CPL et BOM).
- **Conception 3D (Fusion 360) :** 
  - Modélisation sur mesure du boîtier en plastique pour loger proprement le circuit imprimé.
  - Exportation des fichiers de CAO au format universel `.step` et au format source d'archive `.f3d` dans le dossier `CAD`.
- **Nomenclature (BOM) :** Recensement de tous les composants nécessaires avec leurs liens d'achat et calcul du coût total du projet dans le fichier `BOM.csv`.

![Capture d'écran du projet Hackpad](image.png)