IDENTIFICATION DIVISION.
PROGRAM-ID. PolicyReport.
AUTHOR. YourName.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT PolicyIMSFile ASSIGN TO 'POLICYIMS.DAT'
        ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD PolicyIMSFile.
01 PolicyIMSRecord.
   05 Policy-Number-IMS   PIC X(10).
   05 Policy-Data-IMS     PIC X(200).  // Increased the size to accommodate the new fields.

WORKING-STORAGE SECTION.
01 Temp-Record.
   05 Policy-Number-Temp  PIC X(10).
   05 Policy-Holder-Name-Temp  PIC X(50).
   05 Premium-Amount-Temp  PIC 9(9)V99.
   05 Policy-Type-Temp  PIC X(15).  // Increased the size to accommodate the longest policy_type
   05 Coverage-Limits-Temp  PIC 9(9)V99.
   05 Policy-Premium-Temp  PIC 9(9)V99.
   05 Claim-Status-Temp  PIC X(10).

01 WS-Sort-Buffer.
   05 Sort-Key PIC X(10).
   05 Sort-Data PIC X(200).  // Increased the size to accommodate the new fields.

01 Total-Premium-Amount PIC 9(11)V99 VALUE 0.
01 Record-Count         PIC 9(5) VALUE 0.

01 Switch-Variable      PIC X VALUE 'N'.

01 PolicyReportRecord.
   05 Policy-Number       PIC X(10).
   05 Policy-Type         PIC X(15).
   05 Policy-Holder-Name  PIC X(50).
   05 Coverage-Limits     PIC 9(9)V99.
   05 Policy-Premium      PIC 9(9)V99.
   05 Claim-Status        PIC X(10).
   05 Age                 PIC 9(3).
   05 Car-Value           PIC 9(9)V99.
   05 Property-Type       PIC X(20).
   05 Property-Value      PIC 9(9)V99.
   05 Coverage-Amount     PIC 9(9)V99.

01 PolicySummaryReport.
   05 Total-Policies      PIC 9(5) VALUE 0.
   05 Total-Premiums      PIC 9(11)V99 VALUE 0.
   05 Total-Claims        PIC 9(5) VALUE 0.
   05 Total-Rejected-Claims PIC 9(5) VALUE 0.

PROCEDURE DIVISION.
Begin.
    CALL 'DB2-INIT'           // Initialize DB2 connection

    CALL 'FETCH-POLICY-DATA'   // Fetch data from DB2 tables
    CALL 'SORT-POLICY-DATA'    // Sort data in memory

    CALL 'CALCULATE-PREMIUM'   // Calculate total premium amount
    CALL 'GENERATE-REPORT'     // Generate the policy summary report

    CALL 'WRITE-REPORT'        // Write the report to PolicyIMSFile

    CALL 'DB2-CLOSE'          // Close DB2 connection

    STOP RUN.

CALL 'FETCH-POLICY-DATA' USING PolicyDB2File, WS-Sort-Buffer.
CALL 'SORT-POLICY-DATA' USING WS-Sort-Buffer.
CALL 'CALCULATE-PREMIUM' USING Total-Premium-Amount.
CALL 'GENERATE-REPORT' USING PolicyReportRecord, PolicySummaryReport.

CALL 'WRITE-REPORT' USING PolicyIMSFile, PolicyIMSRecord.

STOP RUN.
