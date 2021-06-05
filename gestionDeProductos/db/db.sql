-- ------- Creating database ------
CREATE DATABASE IF NOT EXISTS products;

-- Using db
USE products;

-- Categories table
CREATE TABLE IF NOT EXISTS categories(
id              int(25) auto_increment,
category        varchar(255),

CONSTRAINT      pk_categories PRIMARY KEY(id),
CONSTRAINT      uk_categories UNIQUE(category)
) ENGINE=InnoDb;


-- product table
CREATE TABLE IF NOT EXISTS products(
id              int(12) auto_increment,
product         varchar(75),
category        for
)ENGINE=InnoDb;
