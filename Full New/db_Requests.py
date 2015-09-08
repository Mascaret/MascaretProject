#


########Insertion dans une table "Filtre"

queryAddEmployee = """"START TRANSACTION;

INSERT INTO `mascaretdb6`.`permission` (`idPermission`, `all`) VALUES (NULL, NULL);

SELECT idPermission FROM permission
ORDER BY idPermission DESC
LIMIT 1;

INSERT INTO `mascaretdb6`.`employee` (`idEmployee`, `name`, `surname`, `job`) VALUES ('%d', '%s','%s', '%s');

COMMIT;"""

#####################################
