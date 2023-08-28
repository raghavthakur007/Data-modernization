IDENTIFICATION DIVISION.
PROGRAM-ID. ClaimProcessing.
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
   05 Claim-Status       PIC X(10).

LINKAGE SECTION.
01 ClaimRecord.
   05 Policy-Number      PIC X(10).
   05 Date-of-Loss       PIC X(10).
   05 Cause-of-Loss      PIC X(10).
   05 Amount-of-Loss     PIC 9(9)V99.

PROCEDURE DIVISION USING PolicyDB2File, ClaimRecord.
    PERFORM VARYING Record-Count FROM 1 BY 1
      UNTIL Record-Count > 10
      IF PolicyDB2Record(Record-Count).Policy-Number = ClaimRecord.Policy-Number
          MOVE PolicyDB2Record(Record-Count).Coverage-Limits TO PolicyRecord.Coverage-Limits
          MOVE PolicyDB2Record(Record-Count).Policy-Premium TO PolicyRecord.Policy-Premium
      END-IF
    END-PERFORM.

    IF ClaimRecord.Date-of-Loss > "12/31/2023"
        MOVE "REJECT" TO Claim-Status
    ELSE
        MOVE ClaimRecord.Cause-of-Loss TO PolicyRecord.Policy-Type
        IF PolicyRecord.Policy-Type = "FIRE"
            MOVE 5000 TO ClaimRecord.Amount-of-Loss
        ELSE IF PolicyRecord.Policy-Type = "THEFT"
            MOVE 10000 TO ClaimRecord.Amount-of-Loss
        ELSE IF PolicyRecord.Policy-Type = "FLOOD"
            MOVE 20000 TO ClaimRecord.Amount-of-Loss
        ELSE
            MOVE 0 TO ClaimRecord.Amount-of-Loss
            MOVE "REJECT" TO Claim-Status
        END-IF
        IF ClaimRecord.Amount-of-Loss <= PolicyRecord.Coverage-Limits
            MOVE "PAY" TO Claim-Status
        ELSE
            MOVE "REJECT" TO Claim-Status
        END-IF
    END-IF

    EXIT PROGRAM.
