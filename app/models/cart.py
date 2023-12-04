from flask import current_app as app
import datetime
from .. import login
from .product import Product

class Cart:
    def __init__(self, product_id, product_name, buyer_id,product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.buyer_id = buyer_id
        # self.sell_name = seller_name
        self.product_price = product_price
        # self.seller_name = seller_name
    
  
    
    # buy_now will be displayed in the wishlist!
    @staticmethod
    def get_cart_for_user(buyer_id): 
    # Ensure the SELECT statement fetches all fields required for Cart initialization
        rows = app.db.execute('''
        SELECT Cart.product_id, Products.name, Cart.buyer_id, Products.buy_now As product_price
        FROM Cart, Products
        WHERE 
            Cart.buyer_id = :buyer_id and Cart.product_id = Products.id
        ''', buyer_id=buyer_id)
        return [Cart(*row) for row in rows]


    # @staticmethod
    # def get_cart_for_user(buyer_id):
    # # Ensure the SELECT statement fetches all fields required for Cart initialization
    #     rows = app.db.execute('''
    #     SELECT 
    #         Cart.product_id, 
    #         Products.name, 
    #         Cart.buyer_id, 
    #         Charities.name AS seller_name, 
    #         Products.price AS product_price 
    #     FROM 
    #         Cart
    #     JOIN Products ON Cart.product_id = Products.id
    #     JOIN Sells ON Products.id = Sells.productId
    #     JOIN Charities ON Sells.charityId = Charities.id
    #     WHERE 
    #         Cart.buyer_id = :buyer_id
    #     ''', buyer_id=buyer_id)
    #     return [Cart(*row) for row in rows]
    

    # @staticmethod
    # def get_cart_for_user(buyer_id):
    # # Ensure the SELECT statement fetches all fields required for Cart initialization
    #     rows = app.db.execute('''
    #     SELECT Cart.product_id, Products.name, Cart.buyer_id, Charities.name As seller_name, Products.price As product_price
    #     FROM Cart, Products, Charities
    #     WHERE 
    #         Cart.buyer_id = :buyer_id and Cart.product_id = Products.id
    #     ''', buyer_id=buyer_id)
    #     return [Cart(*row) for row in rows]

    # @staticmethod
    # def get_cart_for_user(buyer_id):
    # # Ensure the SELECT statement fetches all fields required for Cart initialization
    #     rows = app.db.execute('''
    #     SELECT Cart.product_id, Products.name, Cart.buyer_id, Charities.name As seller_name, Products.price As product_price
    #     FROM Cart, Products, Sells, Charities
    #     WHERE 
    #         Cart.buyer_id = :buyer_id and Cart.product_id = Products.id
    #     ''', buyer_id=buyer_id)
    #     return [Cart(*row) for row in rows]

    # @staticmethod
    # def get_cart_for_user(buyer_id):
    # # Ensure the SELECT statement fetches all fields required for Cart initialization
    #     rows = app.db.execute('''
    #     SELECT Cart.product_id, Products.name, Cart.buyer_id
    #     FROM Cart, Products
    #     WHERE 
    #         Cart.buyer_id = :buyer_id and Cart.product_id = Products.id
    #     ''', buyer_id=buyer_id)
    #     return [Cart(*row) for row in rows]
    
    @staticmethod
    def add_to_cart(buy_id, product_id):
        print(f"Attempting to add product {product_id} to cart for user {buy_id}")
    # Check if the product is already in the cart
        rows = app.db.execute('''
        SELECT * FROM Cart WHERE buyer_id=:buy_id AND product_id=:product_id;
        ''', buy_id=buy_id, product_id=product_id)
        print(f"Product already in cart check returned: {rows}")
    # If not in the cart
        if len(rows) == 0:
            app.db.execute('''
            INSERT INTO Cart(product_id, buyer_id)
            VALUES (:product_id, :buy_id);
        ''', product_id=product_id, buy_id=buy_id)
            return "Product added to cart."
    
    # If already in the cart
        else: 
            print(f"Product {product_id} is already in the cart for user {buy_id}")
            return "Product already in the cart."
    
    # @staticmethod   
    # def remove_from_cart(buyer_id, product_id):
    #     affected_rows = app.db.execute('''
    # DELETE FROM Cart 
    # WHERE buyer_id = :buyer_id AND product_id = :product_id;
    # ''', buyer_id=buyer_id, product_id=product_id)
    #     return affected_rows

    @staticmethod
    def remove_from_cart(buyer_id, product_id):
        rows = app.db.execute('''
        DELETE FROM Cart WHERE buyer_id=:buy_id AND Cart.product_id=:product_id;
        ''', buy_id=buyer_id, product_id=product_id)
        return rows


    # @staticmethod
    # def remove_from_cart(buyer_id):
    #     rows = app.db.execute('''DELETE FROM Cart WHERE buyer_id=:buy_id''',
    #                           buy_id=buyer_id)
    #     return rows

