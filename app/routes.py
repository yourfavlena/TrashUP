from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models import TrashImage
from app.feature_extractor import extract_features
from app.rules import classify_image
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    filename = None
    if request.method == 'POST':
        # Annotation manuelle
        if 'annotation' in request.form and 'filename' in request.form:
            img = TrashImage.query.filter_by(filename=request.form['filename']).first()
            if img:
                img.annotation = request.form['annotation']
                db.session.commit()
                flash('Annotation enregistrée !', 'success')
            return redirect(url_for('upload'))
        # Upload d'image
        if 'image' not in request.files:
            flash('Aucun fichier sélectionné', 'danger')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('Aucun fichier sélectionné', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.root_path, 'static', 'uploads', filename)
            file.save(upload_path)
            # Extraction des features
            features = extract_features(upload_path)
            # Classification automatique
            auto_label = classify_image(features)
            # Récupération localisation
            latitude = request.form.get('latitude', type=float)
            longitude = request.form.get('longitude', type=float)
            # Sauvegarde en base
            img = TrashImage(
                filename=filename,
                file_size=features.get('file_size'),
                width=features.get('width'),
                height=features.get('height'),
                avg_red=features.get('avg_red'),
                avg_green=features.get('avg_green'),
                avg_blue=features.get('avg_blue'),
                histogram=features.get('histogram'),
                contrast=features.get('contrast'),
                edges=features.get('edges'),
                luminance_hist=features.get('luminance_hist'),
                annotation=auto_label,
                latitude=latitude,
                longitude=longitude
            )
            db.session.add(img)
            db.session.commit()
            flash(f'Image uploadée et classée automatiquement comme "{auto_label}".', 'info')
            return render_template('upload.html', filename=filename)
        else:
            flash('Format de fichier non autorisé', 'danger')
            return redirect(request.url)
    return render_template('upload.html', filename=filename)

@app.route('/images')
def images():
    all_images = TrashImage.query.order_by(TrashImage.upload_date.desc()).all()
    return render_template('images.html', images=all_images)

@app.route('/image/<int:image_id>')
def image_detail(image_id):
    img = TrashImage.query.get_or_404(image_id)
    return render_template('image_detail.html', img=img) 
from flask import render_template

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

@app.route('/map', methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        # Traitement des données du formulaire
        pass
    return render_template('map.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['fr', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))