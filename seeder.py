#!/usr/bin/env python

import sys
import os
import django
import warnings
import logging

logger = logging.getLogger(__file__)

warnings.filterwarnings("ignore")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rbac.settings')
django.setup()

from django.db import transaction
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import make_password
from users.models import AuthSub


su = User.objects.get(id=1) #superuser
ps = Permission.objects.all() #permissions

try:
	with transaction.atomic():
		su.user_permissions.set(ps)

		subs = [

			User.objects.create(username="sadmin", password=make_password("sadmin@django")),
			User.objects.create(username="xadmin", password=make_password("xadmin@django")),
			User.objects.create(username="zadmin", password=make_password("zadmin@django"))
		]

		for sub in subs:
			AuthSub.objects.create(subordinate=sub, supervisor=su)

	print("Seeder executed successfully.")
except Exception as e:
	logger.critical(e)

	print("Something went horribly wrong!")
