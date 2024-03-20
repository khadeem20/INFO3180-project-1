"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os

from app import app, db
from app.models import Property
from flask import render_template, request, redirect, url_for
from app.forms import  PropertyForm
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash, session, send_from_directory


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
 

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

#The stuff we added

@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    #displays the form to add a new property
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        property_ = Property(
            form.title.data,
            form.numBedrms.data,
            form.numBathrms.data,
            form.location.data,
            form.price.data,
            form.propType.data,
            form.description.data,
            filename
        )
        photo.save(os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename))
        db.session.add(property_)
        db.session.commit()
        flash("Successfully Added")
        return redirect(url_for('properties'))
    return render_template("create_property.html", form=form)


@app.route('/properties')
def display_properties():
    #returns a list of all the properties
    properties = get_properties()
    return render_template("all_properties.html", properties=properties)

def get_properties():
    properties = db.session.query(Property).all()
    return properties 

@app.route('/properties/<propertyid>')
def property(propertyid):
    #for viewing an individual property using its id
    prop = db.session.execute(db.select(Property).filter_by(id=propertyid)).scalar()
    print(prop, propertyid)
    return render_template('all_properties.html', property=prop)
 

