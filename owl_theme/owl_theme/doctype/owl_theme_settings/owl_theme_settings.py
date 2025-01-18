# Copyright (c) 2025, tahirzaqout and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class OwlThemeSettings(Document):
	def validate(self):
		self.change_splash_image_or_favicon()


	def change_splash_image_or_favicon(self):
		# change splash image or favicon in wbsite settings after change in owl theme settings
		if self.has_value_changed("splash_image"):
			self.apply_changes_to_website_settings("splash_image")

		if self.has_value_changed("favicon"):
			self.apply_changes_to_website_settings("favicon")


	def apply_changes_to_website_settings(self, fieldname):
		website_settings = frappe.get_single("Website Settings")
		website_settings.set(fieldname, self.get(fieldname))
		website_settings.save()
		frappe.clear_cache()
