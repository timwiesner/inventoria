from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response, session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests

app = Flask(__name__)


engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Home route
@app.route('/')
@app.route('/inventory')
def showCategories():
    categories = session.query(Category).all()
    return render_template('inventory.html', categories=categories)


# New category
@app.route('/inventory/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        flash('New category created!')
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


# Specific category Route
@app.route('/inventory/<int:category_id>/items')
def showCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('items.html', category=category, items=items)


# Edit category
@app.route('/inventory/edit', methods=['GET', 'POST'])
def editCategory():
    return render_template('editCategory.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
