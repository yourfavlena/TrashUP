from flask import render_template
from app import app, db
from app.models import TrashImage
import matplotlib.pyplot as plt
import io
import base64

@app.route('/dashboard')
def dashboard():
    total_images = TrashImage.query.count()
    pleines = TrashImage.query.filter_by(annotation='pleine').count()
    vides = TrashImage.query.filter_by(annotation='vide').count()
    # Générer un graphique matplotlib
    fig, ax = plt.subplots()
    ax.bar(['Pleine', 'Vide'], [pleines, vides], color=['red', 'blue'])
    ax.set_ylabel('Nombre d\'images')
    ax.set_title('Répartition des annotations')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return render_template('dashboard.html', total_images=total_images, pleines=pleines, vides=vides, img_base64=img_base64)

@app.route('/map')
def map_view():
    images = TrashImage.query.filter(TrashImage.latitude.isnot(None), TrashImage.longitude.isnot(None)).all()
    return render_template('map.html', images=images) 