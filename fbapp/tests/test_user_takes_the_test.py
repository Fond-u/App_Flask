from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import app
from .. import models


class TestUserTakesTheTest(LiveServerTestCase):
	def create_app(self):
		# fichier de config pour les tests
		app.config.from_object('fbapp.tests.config')
		return app

	def setUp(self):
		"""Setup the test driver and creat test users"""
		# le navigateur firefox
		self.driver = webdriver.Firefox()
		# Ajout de données dans la bdd
		models.init_db()

	def tearDown(self):
		self.driver.quit()

	def test_user_login(self):
		self.driver.get(self.get_server_url())

		assert self.driver.current_url == 'http://localhost:8943/'
		