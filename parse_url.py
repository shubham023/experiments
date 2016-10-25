""" utility program for url parsing. Specific for docker registry cases"""
from urlparse import urlparse

def parse_url(url):
	if "http" in url:
		op = urlparse(url)
	
	else :
		url = "http://" + url
		op = urlparse(url)
	print op

def validate_digest(url):
	print "validating digest - NOT IMPLEMENTED YET"

def validate_hostname(hostname):
	print "validating repo - NOT IMPLEMENTED YET"

def validate_port(port):
	print "validating port - NOT IMPLEMENTED YET"

def validate_repo(repo):
	print "validating repo - NOT IMPLEMENTED YET"

def validate_tag(tag):
	print "validating tag - NOT IMPLEMENTED YET"

def parse_url_rev1(url):
	if "@sha256" in url :
		## This is a sha digest not an image. validate digest
		validate_digest(url)

	if "http" not in url and "." not in url:
		# This is just repo name. Use default registry
		url = "http://docker.io:/" + url
		
	if "http" not in url :
		#It is of format localhost.domain or docker.io or 192.168.101.1
		url = "http://" + url

	op = urlparse(url)
	print "hostname : %s" % op.hostname
	if op.port is not None:
		print "port: %s" % op.port
	print "path: %s" % op.path

#parse_url("localhost.localdomain:5000/ubuntu")
#parse_url("http://localhost.localdomain:5000/ubuntu")

parse_url_rev1("localhost.localdomain:5000/ubuntu")
parse_url_rev1("ubuntu")
parse_url_rev1("ubuntu:latest")
parse_url_rev1("localhost.localdomain:5000/ubuntu:latest")
parse_url_rev1("http://localhost.localdomain:5000/ubuntu")
parse_url_rev1("http://localhost.localdomain:5000/ubuntu:latest")
parse_url_rev1("@sha256: c73a085dc3782b3fd4c032971c76d6afb45fa3728a048175c8c77d7403de5f21 ")
parse_url_rev1("http://192.168.122.1:5000/ubuntu:latest")
parse_url_rev1("192.168.121.102:5000/ubuntu:latest")
