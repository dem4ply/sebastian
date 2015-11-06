from django.test.runner import DiscoverRunner
from django.utils import unittest
from unittest.suite import TestSuite

class Customized_runner( DiscoverRunner ):
	def build_suite( self, *args, **kwargs ):
		suite = super( Customized_runner, self ).build_suite( *args, **kwargs )
		filtered = TestSuite()

		for test in suite:
			if self.package in str( test ):
				filtered.addTest( test )
		return filtered

class Unit_runner( Customized_runner ):
	package = '.unit.'

	def setup_databases( self, *args, **kwargs ):
		return

	def teardown_databases( self, *args, **kwargs ):
		return

class Integration_runner( Customized_runner ):
	package = '.integration.'

class Acceptance_runner( Customized_runner ):
	package = '.acceptance.'
