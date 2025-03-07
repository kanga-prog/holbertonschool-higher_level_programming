-- 1-create_and_grant_user.sql

-- Créer l'utilisateur 'user_0d_1' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges à 'user_0d_1' sur toutes les bases de données
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Appliquer les modifications en rechargeant les privilèges
FLUSH PRIVILEGES;

