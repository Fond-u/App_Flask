import random

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

from fbapp.models import Content, Gender

def find_content(gender):
	contents = Content.query.filter(Content.gender == Gender[gender]).all()
	return random.choice(contents)

class OpenGraphImage :

	def __init__(self, uid, first_name, description):
		self.location = self._location(uid)
		background = self.base()
		self.print_on_img(background, first_name.capitalize(), 70, 50)
		#description
		sentences = textwrap.wrap(description, width=60 )

		current_h, pad = 180, 10
		for sentence in sentences:
			w, h =self.print_on_img(background, sentence, 40, current_h)
			current_h += h + pad

		background.save(self._path(uid))

	def base(self):
		img = Image.new('RGB', (1200,630), '#18BC9C')
		return img

	def print_on_img(self, img, text, size, height):
		# chargement de la police
		font = ImageFont.truetype(os.path.join('fbapp','static', 'fonts', 'Arcon-Regular.otf'), size)

		#creation nouvelle instance
		draw = ImageDraw.Draw(img)

		#calcul de la taille du text en pixel (largeur, hauteur)
		w,h = draw.textsize(text, font)

		#calcul de la position du text centré
		position = ((img.width - w)/2, height)

		#ajoute le texte a l'image
		draw.text(position, text, (255, 255, 255), font=font)

		return (w,h)

	def _path(self, uid):
		return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(uid))

	def _location(self, uid):
		return 'tmp/{}.jpg'.format(uid)

