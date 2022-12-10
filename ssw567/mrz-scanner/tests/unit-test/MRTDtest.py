import unittest
from for_test_MRTD import *

class TestMRTD(unittest.TestCase):
    # Define test cases that input has two line or not
    scanInfo="P<REUMCFARLAND<<TRINITY<AMITY<<<<<<<<<<<<<<<;Q683170H11REU6403131M6904133UK128819I<<<<<<9"
    dbInfo=["P","REU","MCFARLAND","TRINITY","AMITY","Q683170H1","REU",640313,"M",690413,"UK128819I"]
    #this test case is for scanMRZ
    def testScanMRZ(self):
        self.assertEqual(scanMRZ(),scanInfo,"SCAN DECODED DATA ")

    #this test case is for getting data from database
    def testGetFromDatabase(self):
        self.assertEqual(getFromDatabase(),dbInfo, "DATABASE is CORRECT")

    #this is test case for decode string
    def testDecodeString(self):
        self.assertEqual(decodeStrings(scanInfo),(['P','REU','MCFARLANDTRINITYAMITY'],['Q683170H1','1','REU','640313','1','M','690413','3','UK128819I','9']),'DECODED STRING IN CORRECT FORMAT')

    #this test case for checking valid all digit number
    def testCalcCheck(self):
        self.assertEqual(calcCheck(dbInfo),([1, 1, 3, 9]),"valid all digit")

    #this test case for checking valid for PASSPORT number
    def testCalcCheckA(self):
        self.assertEqual(calcCheck(dbInfo)[0], 1, "valid PASSPORT number")

    #this test case for checking valid for BIRTHDATE number
    def testCalcCheckB(self):
        self.assertEqual(calcCheck(dbInfo)[1], 1, "valid BIRTHDATE number")

    #this test case for checking valid for EXPIRATION DATE number
    def testCalcCheckC(self):
        self.assertEqual(calcCheck(dbInfo)[2], 3, "valid EXPIRATION DATE number")

    #this test case for checking valid for PERSONAL number
    def testCalcCheckD(self):
        self.assertEqual(calcCheck(dbInfo)[3], 9, "valid PERSONAL number")

    #this test for checking that string is ENCODED OR NOT
    def testEncodeStrings(self):
        self.assertEqual(encodeStrings(dbInfo),scanInfo, "string is ENCODED OR NOT")

    #this test case is for comparison of ENCODED and DECODED data
    def testReportDiffrence(self):
        self.assertEqual(reportDifference(scanInfo,dbInfo),"Database Matches Scanned Record","comparison of ENCODED and DECODED data")

    #this test case is for not getting any error of mismatched PASSPORT number
    def testReportDiffrenceA(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Line 2 from the database does not match what was scanned check digit 1 did not match", "not getting any error of mismatched PASSPORT number")

    #this test case is for not getting any error of mismatched BIRTHDATE number
    def testReportDiffrenceB(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Line 2 from the database does not match what was scanned check digit 2 did not match", "not getting any error of mismatched BIRTHDATE number")

    #this test case is for not getting any error of mismatched EXPIRATION DATE number
    def testReportDiffrenceC(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Line 2 from the database does not match what was scanned check digit 3 did not match", "not getting any error of mismatched EXPIRATION DATE number")

    #this test case is for not getting any error of mismatched PERSONAL number
    def testReportDiffrenceD(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Line 2 from the database does not match what was scanned check digit 4 did not match", "not getting any error of mismatched PERSONAL number")

    #this test case is for not getting any error of mismatched of LINE1 code with our DECODED CODE
    def testReportDiffrenceE(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Line 1 from the database does not match what was scanned", "not getting any error of mismatched of LINE1 code with our DECODED CODE")

    #this test case is for not getting any error of mismatched of EITHER LINE from OUR DATA
    def testReportDiffrenceF(self):
        self.assertNotEqual(reportDifference(scanInfo,dbInfo),"Neither Line from the database matches what was scanned", "not getting any error of mismatched of EITHER LINE from OUR DATA")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
