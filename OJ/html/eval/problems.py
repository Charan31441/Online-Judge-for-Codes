# Contains information about test data for problems

TEST_ROOT = "/var/www/html/eval/eval/"   # The location where test cases input/output files are located on your system. Absolute Path.

# 'testcases' should map problemID to a list of test cases.
# Each test case is a tuple in following format.
# ( inputFilename, outputfilename, score, memory limit in MBs, time limit in secs)

testcases = {
	"P1" : [ ("inp1_1","out1_1",30,32,1),("inp1_2","out1_2",30,32,1),("inp1_3","out1_3",40,32,1)],

	"P2" : [ ("inp2_1","out2_1",30,32,1),("inp2_2","out2_2",30,32,1),("inp2_3","out2_3",40,32,1) ],

	}

# 'checker' should map problemID to a program name that is to be used to check out.
# You can code checker as per your need. They are simple C/CPP programs that take as argument two filenames locally available.
# The first file is, JUDGE output and second is contestant solution. If your problem has no JUDGE output, use a empty file and dont use it latter on.
# The program as its exit code ( return '0' / return '1' ) should return verdict as correct (0) or wrong (!0).
#
# By default, we provide a simple checker, exact.out that checks character by character.

checker  = {"P1":"exact.out","P2":"exact.out"}
