IDENTIFICATION DIVISION.
PROGRAM-ID. GenerateReport.
AUTHOR. Udit Sharma.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 PolicyRecord.
   05 Policy-Number      PIC X(10).
   05 Policy-Holder-Name PIC X(50).
   05 Premium-Amount     PIC 9(9)V99.
   05 Policy-Type        PIC X(15).  // Increased the size to accommodate the longest policy_type
   05 Coverage-Limits    PIC 9(9)V99.
   05 Policy-Premium     PIC 9(9)V99.
   05 Age                PIC 9(3).
   05 Car-Value          PIC 9(9)V99.
   05 Property-Type      PIC X(20).
   05 Property-Value     PIC 9(9)V99.
   05 Coverage-Amount    PIC 9(9)V99.

LINKAGE SECTION.
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

PROCEDURE DIVISION USING PolicyReportRecord, PolicySummaryReport.
    DISPLAY "Generating policy summary report..."
    MOVE Policy-Premium TO Premium-Amount-Temp
    ADD Premium-Amount-Temp TO Total-Premiums
    ADD 1 TO Total-Policies

    IF Claim-Status = "PAY"
        ADD 1 TO Total-Claims
    ELSE
        ADD 1 TO Total-Rejected-Claims
    END-IF

    MOVE Policy-Number TO PolicyIMSRecord.Policy-Number-IMS
    MOVE Policy-Holder-Name TO PolicyIMSRecord.Policy-Data-IMS
    MOVE Policy-Type TO PolicyIMSRecord.Policy-Type-IMS
    MOVE Coverage-Limits TO PolicyIMSRecord.Coverage-Limits-IMS
    MOVE Policy-Premium TO PolicyIMSRecord.Policy-Premium-IMS
    MOVE Age TO PolicyIMSRecord.Age-IMS
    MOVE Car-Value TO PolicyIMSRecord.Car-Value-IMS
    MOVE Property-Type TO PolicyIMSRecord.Property-Type-IMS
    MOVE Property-Value TO PolicyIMSRecord.Property-Value-IMS
    MOVE Coverage-Amount TO PolicyIMSRecord.Coverage-Amount-IMS

    // Add other fields to PolicyIMSRecord as required for the report

    MOVE PolicyIMSRecord TO PolicyIMSFile
    WRITE PolicyIMSRecord TO PolicyIMSFile

    DISPLAY "Policy summary report generated."
    EXIT PROGRAM.
