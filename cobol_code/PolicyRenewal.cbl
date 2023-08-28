IDENTIFICATION DIVISION.
PROGRAM-ID. PolicyRenewal.
AUTHOR. Udit Sharma.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 PolicyRecord.
   05 Policy-Number      PIC X(10).
   05 Policy-Holder-Name PIC X(50).
   05 Premium-Amount     PIC 9(9)V99.
   05 Policy-Type        PIC X(15).  
   05 Coverage-Limits    PIC 9(9)V99.
   05 Policy-Premium     PIC 9(9)V99.

LINKAGE SECTION.
01 PolicyDB2File.
   05 PolicyDB2Record OCCURS 10 TIMES.
      10 Policy-Number      PIC X(10).
      10 Policy-Holder-Name PIC X(50).
      10 Premium-Amount     PIC 9(9)V99.
      10 Policy-Type        PIC X(15).  
      10 Coverage-Limits    PIC 9(9)V99.
      10 Policy-Premium     PIC 9(9)V99.

PROCEDURE DIVISION USING PolicyDB2File.
    PERFORM VARYING Record-Count FROM 1 BY 1
      UNTIL Record-Count > 10
      MOVE Policy-Type TO PolicyRecord.Policy-Type
      IF PolicyRecord.Policy-Type = "CAR_INSURANCE"
          MOVE 200000 TO PolicyRecord.Coverage-Limits
          MOVE 1200 TO PolicyRecord.Policy-Premium
      ELSE IF PolicyRecord.Policy-Type = "HOME_INSURANCE"
          MOVE 600000 TO PolicyRecord.Coverage-Limits
          MOVE 2400 TO PolicyRecord.Policy-Premium
      ELSE IF PolicyRecord.Policy-Type = "LIFE_INSURANCE"
          MOVE 1200000 TO PolicyRecord.Coverage-Limits
          MOVE 3600 TO PolicyRecord.Policy-Premium
      ELSE
          MOVE 0 TO PolicyRecord.Coverage-Limits
          MOVE 0 TO PolicyRecord.Policy-Premium
      END-IF
      MOVE PolicyRecord.Coverage-Limits TO Coverage-Limits(Record-Count)
      MOVE PolicyRecord.Policy-Premium TO Policy-Premium(Record-Count)
    END-PERFORM.
    EXIT PROGRAM.
