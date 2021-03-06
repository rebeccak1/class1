#Convert to 4 columns for calculating likelihood
from math import *
import glob
import numpy as np
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-i', metavar = 'N', type = 'string', action = 'store', default = '', dest = 'i', help='input filename')

parser.add_option('-o', metavar = 'N', type = 'string', action = 'store', default = '', dest = 'o', help='output filename')

(options, args) = parser.parse_args()

def writecls(f, l, spectrum):
	if spectrum == 'TT':
		index = 1

	print(len(l))
	#for i in range(len(l)):
	for i in range(0,28):
		#f.write(str(l[i][index]) + '\n')
		f.write(str(2.*3.14159*l[i][index]/(l[i][0]*(l[i][0] + 1.))) + '\n')

def likformat(filename):#, outfname):
	f = open(filename, 'r')
	#outf = open('TElikcls_hil/' + filename[filename.rfind('/')+1:filename.rfind('.')] + '_likcls.txt', 'w')
	outf = open('lowlmp.txt', 'w')
	lines = f.readlines()
	for i in range(len(lines)):

		lines[i] = lines[i].strip().split()[:2]
		
		lines[i] = [float(lines[i][0]), float(lines[i][1])]
		#class
		#lines[i] = [float(lines[i][0]), float(lines[i][1]), float(lines[i][2]), float(lines[i][3])]

	outf.write('0\n0\n')
	writecls(outf, lines, 'TT')

	#outf.write("0.9980537") #A_planck
	outf.write("1.0") #A_planck

	outf.close()
	f.close()

def main():
	#nov25	
	#ds = np.linspace(0.018, 0.028, 11) 
	#cs = np.linspace(1.e-3, 2.e-3, 40) 
	#bs = np.linspace(10., 20., 40) 

	#jan5
	ds = 10**(np.linspace(np.log10(0.0012), np.log10(0.028), 20))
	cs = np.linspace(1.e-3, 2.e-3, 20) 
	bs = np.log10(np.linspace(10**14., 10**15., 10))

	files = ['../montepython_public-2.2.1/unlensedcls.txt']
	#files = ['output/montepython02_cl.dat']
	#files = glob.glob("*dat")
	l = len(files)
	print l
	for m in range(l):
		#print int(.1*l)
		#if (m+1)%int(.1*l) == 0:
		#	print 'Done ' + str(100.*float(m+1)/float(l)) + '%'
		likformat(files[m])
	#likformat(options.i, options.o)
main()
