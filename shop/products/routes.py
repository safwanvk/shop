import secrets

from flask import render_template, request, flash, url_for, session

from shop import app
from werkzeug.utils import redirect

from .forms import AddProductForm
from .models import Brand, Category, Product
from .. import db, photos


@app.route('/add-brand', methods=['GET', 'POST'])
def add_brand():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        get_brand = request.form['brand']
        brand = Brand(name=get_brand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {get_brand} was added to your database', 'success')
        return redirect(url_for('add_brand'))
    return render_template('products/add_brand.html', brands='brands')


@app.route('/update-brand/<int:id>', methods=['GET', 'POST'])
def update_brand(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    update_brand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        update_brand.name = brand
        flash(f'Your brand has been updated', 'success')
        db.session.commit()
        return redirect(url_for('view_brands'))
    return render_template('products/update_brand.html', update_brand=update_brand)


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        get_category = request.form['category']
        category = Category(name=get_category)
        db.session.add(category)
        db.session.commit()
        flash(f'The Category {get_category} was added to your database', 'success')
        return redirect(url_for('add_category'))
    return render_template('products/add_brand.html')


@app.route('/update-category/<int:id>', methods=['GET', 'POST'])
def update_category(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    update_category = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        update_category.name = category
        flash(f'Your category has been updated', 'success')
        db.session.commit()
        return redirect(url_for('view_categories'))
    return render_template('products/update_brand.html', update_category=update_category)


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProductForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')
        addpro = Product(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc,
                         brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        flash(f'The product {name} has been added to your database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/add_product.html', form=form, brands=brands, categories=categories)


@app.route('/update-product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Product.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = AddProductForm(request.form)
    if request.method == 'POST':
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.brand_id = brand
        product.category_id = category
        product.colors = form.colors.data
        product.desc = form.discription.data
        db.session.commit()
        flash(f'Your product has been updated', 'success')
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.desc
    return render_template('products/update_product.html', form=form, brands=brands, categories=categories, product=product)