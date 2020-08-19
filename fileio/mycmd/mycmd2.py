#coding=utf-8

# $ python3 mycmd2.py -h
# usage: mycmd2.py -i <inputfile> -o <outputfile>
#
# $ python3 mycmd2.py -i inputfile -o outputfile
# 输入的文件为： inputfile
# 输出的文件为： outputfile

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="]) #第二个参数通过:分割参数，第一个hi表示可以输入h或i,o表示第二个参数是o
                                                                   #打三个参数表示另外可以使用的选项，用--k=v的方式替换前面的hi:o
   except getopt.GetoptError:
      print ('xxx')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('mycmd2.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('输入的文件为：', inputfile)
   print ('输出的文件为：', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])