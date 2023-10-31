-- Feel free to modify this file to match your development goal.
-- Here we only create 3 tables for demo purpose.

CREATE TABLE Users (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    balance FLOAT NOT NULL
);

CREATE TABLE Charities (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    orgId INT NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
    name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Charity(charity_user_id, org_id)

CREATE TABLE Products (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    name VARCHAR(255) UNIQUE NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    catergory VARCHAR(255),
    expiration timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
    image VARCHAR NOT NULL,
    rating DECIMAL(12,2) NOT NULL
);

CREATE TABLE Sells (
    charityId INT NOT NULL REFERENCES Charities(id),
    productId INT NOT NULL REFERENCES Products(id),
    PRIMARY KEY(charityId, productId)
);

CREATE TABLE Sells (
    charityId INT NOT NULL REFERENCES Charities(id),
    productId INT NOT NULL REFERENCES Products(id),
    PRIMARY KEY(charityId, productId)
);

CREATE TABLE Purchases (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    --Should I create a name column?
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);

CREATE TABLE Cart (
    cart_item_id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    user_id INT NOT NULL REFERENCES Users(id),
    quantity INT NOT NULL,
    status VARCHAR(50) NOT NULL -- Possible values could be 'In Cart', 'Checked Out', etc.
);

CREATE TABLE Wishlist (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    time_added timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);

CREATE TABLE Reviews (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    date_posted timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
    feedback TEXT NOT NULL,
    CONSTRAINT only_one_review_per_product_review UNIQUE (uid, pid)
);
