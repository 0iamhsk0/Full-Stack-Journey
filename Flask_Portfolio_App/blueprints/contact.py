from flask import Blueprint, render_template, request, flash
import json

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        print('Contact Form Submission:', data)
        flash('Thank you for contacting!')
    return render_template('contact.html')
