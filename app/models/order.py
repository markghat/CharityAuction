from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask import jsonify

from .product import Product

from flask import current_app as app

from flask import Blueprint
bp = Blueprint('order', __name__)




class Order:
    def __init__(self, orderId, purchaseId, productName, buyerId, charityId, date_placed, cost, status):
        self.id = orderId
        self.purchaseId = purchaseId
        self.productName = productName
        self.buyerId = buyerId
        self.charityId = charityId
        self.date_placed = date_placed
        self.cost = cost
        self.status = status

    #Orders(purchaseId, productName, buyerId, sellerId, date_placed, total_cost, status)

    # id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    # purchaseId INT NOT NULL REFERENCES Purchases(id),
    # productName VARCHAR(255) UNIQUE NOT NULL,
    # buyerId INT NOT NULL REFERENCES Users(id),
    # sellerId INT NOT NULL REFERENCES Users(id),
    # date_placed timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
    # total_cost DECIMAL(12,2) NOT NULL,
    # status BOOLEAN DEFAULT FALSE

    #returns order by id
    @staticmethod
    def get(id):
        rows = app.db.execute('''
            SELECT *
            FROM Orders
            WHERE id = :id
        ''', id=id)
        return Order(*rows[0]) if rows else None

    #adds order to table
    @staticmethod
    def add_order(purchaseId, productName, buyerId, charityId, date_placed, cost, status): #!!!subtract balance by cost of prduct (come back)
        try:
            rows = app.db.execute("""
INSERT INTO Orders(purchaseId, productName, buyerId, sellerId, date_placed, total_cost, status)
VALUES(:purchaseId, :productName, :buyerId, :charityId,:date_placed, :cost,:status)
RETURNING id
""",
                                  purchaseId=purchaseId,
                                  productName=productName,
                                  buyerId=buyerId,
                                  charityId = charityId,
                                  date_placed = date_placed,
                                  cost = cost,
                                  status = status
                                  )

            #return Order.get(id)
            return
        except Exception as e:
            # likely email already in use; better error checking and reporting needed;
            # the following simply prints the error to the console:
            print(str(e))
            return None

    #toggle's boolean fullfillment status
    @staticmethod
    def change_fulfillment_status(oid, newStatus): #!!!subtract balance by cost of prduct (come back)
        try:
            rows = app.db.execute("""
        UPDATE Orders
        SET status = :newStatus
        WHERE id = :oid
    """, newStatus = newStatus, oid=oid)

            print('new status made for this order item!! :D')
            print(newStatus)
            print("\n")

            #return Order.get(id)
            return
        except Exception as e:
            # likely email already in use; better error checking and reporting needed;
            # the following simply prints the error to the console:
            print(str(e))
            return None
    
